
import csv
import json
import os
import sys


def csv_to_json(csv_path, json_path):
    # newline="" ensures standard line-endings across platforms (Windows vs Mac/Linux)
    # encoding="utf-8" ensures full Unicode compatibility for special characters
    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    with open(json_path, mode="w", newline="", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


def json_to_csv(json_path, csv_path):
    with open(json_path, mode="r", newline="", encoding="utf-8") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            print("Error: Invalid JSON syntax.", file=sys.stderr)
            sys.exit(1)

    # Acceptance criteria verification: Make sure it's a list of flat dictionaries
      # If the JSON is a single flat object, wrap it in a list to make it compatible with DictWriter
    if isinstance(data, dict):
        data = [data]

    # Acceptance criteria verification: Make sure it's a list of flat objects
    if not isinstance(data, list) or not all(
        isinstance(item, dict) for item in data
    ):
        print(
            "Error: JSON input must be a list of flat objects.", file=sys.stderr
        )
        sys.exit(1)


    if not data:
        print("Warning: JSON file is empty.", file=sys.stderr)
        return

    # Extract column names from keys of the first item
    headers = data[0].keys()

    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python scripts/csv_json_converter.py <input_file> <output_file>",
            file=sys.stderr,
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate file existence
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)

    # Automatically handle conversion logic based on file extension rules
    if input_file.endswith(".csv") and output_file.endswith(".json"):
        csv_to_json(input_file, output_file)
    elif input_file.endswith(".json") and output_file.endswith(".csv"):
        json_to_csv(input_file, output_file)
    else:
        print(
            "Error: Invalid extensions. Use .csv -> .json or .json -> .csv",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()

