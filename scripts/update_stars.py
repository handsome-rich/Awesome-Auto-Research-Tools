"""
Fetch latest GitHub star counts and re-sort README tables.

Usage:
    python scripts/update_stars.py          # dry-run, print changes
    python scripts/update_stars.py --apply  # write changes to files
"""

import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

READMES = ["README.md", "README_CN.md"]
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
STAR_THRESHOLD = 500
API_BASE = "https://api.github.com/repos"

HEADERS = {"Accept": "application/vnd.github.v3+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def get_stars(owner: str, repo: str) -> int | None:
    """Return current star count, or None on failure."""
    url = f"{API_BASE}/{owner}/{repo}"
    for attempt in range(3):
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            return resp.json()["stargazers_count"]
        if resp.status_code == 403:  # rate limit
            reset = int(resp.headers.get("X-RateLimit-Reset", 0))
            wait = max(reset - int(time.time()), 5)
            print(f"  Rate limited, waiting {wait}s ...")
            time.sleep(wait)
            continue
        if resp.status_code == 404:
            print(f"  WARNING: {owner}/{repo} not found (404)")
            return None
        print(f"  WARNING: {owner}/{repo} returned {resp.status_code}")
        return None
    return None

# ---------------------------------------------------------------------------
# README parsing
# ---------------------------------------------------------------------------

# Match table rows like:
# | [Name](https://github.com/owner/repo) | ![Stars](...) | ... |
ROW_RE = re.compile(
    r"^\|[^|]*\[.*?\]\(https://github\.com/([^/]+)/([^/)]+)\)"
)

DATE_RE = re.compile(
    r"(\*\*(?:📅\s*)?(?:Star counts last verified|Star 数据最后验证时间)[:：]\s*)(\d{4}-\d{2}-\d{2})(\*\*)"
)


def extract_repos_from_readme(path: str) -> list[tuple[str, str]]:
    """Return list of (owner, repo) found in table rows."""
    repos = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ROW_RE.match(line.strip())
            if m:
                owner, repo = m.group(1), m.group(2)
                if (owner, repo) not in repos:
                    repos.append((owner, repo))
    return repos


def sort_section_by_stars(lines: list[str], star_map: dict) -> list[str]:
    """
    Given the full file as a list of lines, find each markdown table and
    re-sort its data rows by star count (descending).
    Returns new list of lines.
    """
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect table header row (starts with |)
        if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].startswith("|--"):
            # Collect header + separator
            header = line
            separator = lines[i + 1]
            result.append(header)
            result.append(separator)
            i += 2

            # Collect data rows
            data_rows = []
            while i < len(lines) and lines[i].startswith("|"):
                data_rows.append(lines[i])
                i += 1

            # Sort by star count
            def row_star_key(row):
                m = ROW_RE.match(row.strip())
                if m:
                    key = f"{m.group(1)}/{m.group(2)}"
                    return star_map.get(key, 0)
                return 0

            data_rows.sort(key=row_star_key, reverse=True)
            result.extend(data_rows)
        else:
            result.append(line)
            i += 1

    return result


def update_date(lines: list[str], new_date: str) -> list[str]:
    """Update the 'last verified' date."""
    updated = []
    for line in lines:
        updated.append(DATE_RE.sub(rf"\g<1>{new_date}\g<3>", line))
    return updated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    apply = "--apply" in sys.argv

    # 1. Collect all unique repos from both READMEs
    all_repos: list[tuple[str, str]] = []
    for readme in READMES:
        if os.path.exists(readme):
            for r in extract_repos_from_readme(readme):
                if r not in all_repos:
                    all_repos.append(r)

    print(f"Found {len(all_repos)} repos to check.\n")

    # 2. Fetch star counts
    star_map: dict[str, int] = {}  # "owner/repo" -> stars
    below_threshold = []

    for owner, repo in all_repos:
        stars = get_stars(owner, repo)
        key = f"{owner}/{repo}"
        if stars is not None:
            star_map[key] = stars
            status = "BELOW THRESHOLD" if stars < STAR_THRESHOLD else "ok"
            print(f"  {key}: {stars:,} {status}")
            if stars < STAR_THRESHOLD:
                below_threshold.append((key, stars))
        else:
            star_map[key] = 0
            print(f"  {key}: FAILED")
        time.sleep(0.5)  # be polite

    # 3. Report
    print(f"\n{'='*60}")
    print(f"Total repos: {len(all_repos)}")
    if below_threshold:
        print(f"\n⚠️  Projects below {STAR_THRESHOLD} stars:")
        for key, stars in below_threshold:
            print(f"   {key}: {stars}")
    print()

    # 4. Update READMEs
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    changed = False

    for readme in READMES:
        if not os.path.exists(readme):
            continue

        with open(readme, encoding="utf-8") as f:
            original = f.read()
            lines = original.splitlines(keepends=True)

        # Re-sort tables
        lines = sort_section_by_stars(lines, star_map)
        # Update date
        lines = update_date(lines, today)

        new_content = "".join(lines)

        if new_content != original:
            changed = True
            print(f"📝 {readme}: changes detected")
            if apply:
                with open(readme, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"   ✅ Written.")
            else:
                print(f"   (dry-run, use --apply to write)")
        else:
            print(f"📝 {readme}: no changes needed")

    if not changed:
        print("\n✅ Everything up to date, no changes needed.")

    # Set output for GitHub Actions
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
