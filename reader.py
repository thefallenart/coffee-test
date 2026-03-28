import csv


class FileReadError(Exception):
    pass


def read_files(file_paths):
    data = []

    for file_path in file_paths:
        try:
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)

                required_fields = {"student", "coffee_spent"}
                if not reader.fieldnames or not required_fields.issubset(reader.fieldnames):
                    raise FileReadError(
                        f"{file_path}: missing required columns {required_fields}"
                    )

                for i, row in enumerate(reader, start=2):
                    try:
                        row["coffee_spent"] = int(row["coffee_spent"])
                    except (ValueError, TypeError):
                        raise FileReadError(
                            f"{file_path}: invalid coffee_spent at line {i}"
                        )

                    data.append(row)

        except FileNotFoundError:
            raise FileReadError(f"File not found: {file_path}")

    if not data:
        raise FileReadError("No data loaded from files")

    return data
