import argparse
import sys
from tabulate import tabulate

from reader import read_files, FileReadError
from reports import REPORTS
from reports.median_coffee import ReportError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    try:
        if args.report not in REPORTS:
            raise ValueError(f"Unknown report: {args.report}")

        data = read_files(args.files)
        result = REPORTS[args.report](data)

        print(tabulate(result, headers="keys", tablefmt="grid"))

    except (FileReadError, ReportError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()