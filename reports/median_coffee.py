from collections import defaultdict
from statistics import median


class ReportError(Exception):
    pass


def generate(data):
    if not data:
        raise ReportError("Empty dataset")

    student_coffee = defaultdict(list)

    for row in data:
        student = row.get("student")
        coffee = row.get("coffee_spent")

        if student is None or coffee is None:
            raise ReportError("Invalid row structure")

        student_coffee[student].append(coffee)

    result = []

    for student, values in student_coffee.items():
        if not values:
            continue

        result.append({
            "student": student,
            "median_coffee": int(median(values))
        })

    if not result:
        raise ReportError("No valid data to build report")

    result.sort(key=lambda x: x["median_coffee"], reverse=True)

    return result
