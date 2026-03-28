import subprocess
import sys


def test_cli_success(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "student,coffee_spent\nA,100\nA,200\n",
        encoding="utf-8"
    )

    result = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files", str(file),
            "--report", "median-coffee"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "A" in result.stdout


def test_cli_unknown_report(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "student,coffee_spent\nA,100\n",
        encoding="utf-8"
    )

    result = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--files", str(file),
            "--report", "unknown"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 1
    assert "Unknown report" in result.stderr
