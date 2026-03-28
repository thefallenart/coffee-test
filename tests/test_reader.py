import pytest
from reader import read_files, FileReadError


def test_read_valid_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "student,coffee_spent\nA,100\nA,200\n",
        encoding="utf-8"
    )

    data = read_files([file])

    assert len(data) == 2
    assert data[0]["coffee_spent"] == 100


def test_file_not_found():
    with pytest.raises(FileReadError):
        read_files(["no_file.csv"])


def test_missing_column(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("student\nA\n", encoding="utf-8")

    with pytest.raises(FileReadError):
        read_files([file])


def test_invalid_coffee_value(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "student,coffee_spent\nA,abc\n",
        encoding="utf-8"
    )

    with pytest.raises(FileReadError):
        read_files([file])


def test_empty_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("student,coffee_spent\n", encoding="utf-8")

    with pytest.raises(FileReadError):
        read_files([file])
