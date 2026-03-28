import pytest
from reports.median_coffee import generate, ReportError


def test_single_student():
    data = [
        {"student": "A", "coffee_spent": 100},
        {"student": "A", "coffee_spent": 300},
        {"student": "A", "coffee_spent": 200},
    ]

    result = generate(data)

    assert result == [{"student": "A", "median_coffee": 200}]


def test_multiple_students_sorted():
    data = [
        {"student": "A", "coffee_spent": 100},
        {"student": "A", "coffee_spent": 200},
        {"student": "B", "coffee_spent": 500},
        {"student": "B", "coffee_spent": 600},
    ]

    result = generate(data)

    assert result[0]["student"] == "B"
    assert result[1]["student"] == "A"


def test_even_count_median():
    data = [
        {"student": "A", "coffee_spent": 100},
        {"student": "A", "coffee_spent": 200},
    ]

    result = generate(data)

    assert result[0]["median_coffee"] == 150


def test_empty_data():
    with pytest.raises(ReportError):
        generate([])


def test_invalid_row():
    data = [{"student": "A"}]

    with pytest.raises(ReportError):
        generate(data)
