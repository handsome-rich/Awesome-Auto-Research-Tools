import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import update_stars


class UpdateStarsTests(unittest.TestCase):
    def test_sort_section_by_stars_sorts_each_table_descending(self):
        lines = [
            "| Project | Stars |\n",
            "|---------|-------|\n",
            "| [Low](https://github.com/example/low) | badge |\n",
            "| [High](https://github.com/example/high) | badge |\n",
            "\n",
        ]

        result = update_stars.sort_section_by_stars(
            lines,
            {"example/low": 500, "example/high": 1_000},
        )

        self.assertEqual(result[2], "| [High](https://github.com/example/high) | badge |\n")
        self.assertEqual(result[3], "| [Low](https://github.com/example/low) | badge |\n")

    def test_update_date_handles_both_readme_labels(self):
        lines = [
            "**📅 Star counts last verified: 2020-01-01**\n",
            "**📅 Star 数据最后验证时间：2020-01-01**\n",
        ]

        result = update_stars.update_date(lines, "2026-07-25")

        self.assertEqual(
            result,
            [
                "**📅 Star counts last verified: 2026-07-25**\n",
                "**📅 Star 数据最后验证时间：2026-07-25**\n",
            ],
        )

    @patch("scripts.update_stars.time.sleep")
    @patch("scripts.update_stars.time.time", return_value=1_000)
    @patch("scripts.update_stars.requests.get")
    def test_get_stars_does_not_wait_for_long_rate_limit(
        self,
        mock_get,
        _mock_time,
        mock_sleep,
    ):
        mock_get.return_value = Mock(
            status_code=403,
            headers={"X-RateLimit-Reset": "1061"},
        )

        result = update_stars.get_stars("example", "repo")

        self.assertIsNone(result)
        mock_sleep.assert_not_called()

    def test_main_leaves_readme_unchanged_when_any_fetch_fails(self):
        original = (
            "**📅 Star counts last verified: 2020-01-01**\n\n"
            "| Project | Stars |\n"
            "|---------|-------|\n"
            "| [Repo](https://github.com/example/repo) | badge |\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            readme = Path(temp_dir, "README.md")
            readme.write_text(original, encoding="utf-8")

            with (
                patch.object(update_stars, "READMES", ["README.md"]),
                patch.object(update_stars, "get_stars", return_value=None),
                patch("scripts.update_stars.time.sleep"),
                patch("scripts.update_stars.sys.argv", ["update_stars.py", "--apply"]),
                patch.dict(os.environ, {"GITHUB_OUTPUT": ""}),
            ):
                previous_cwd = os.getcwd()
                os.chdir(temp_dir)
                try:
                    exit_code = update_stars.main()
                finally:
                    os.chdir(previous_cwd)

            self.assertEqual(exit_code, 1)
            self.assertEqual(readme.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
