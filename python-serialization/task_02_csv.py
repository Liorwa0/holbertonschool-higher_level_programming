#!/usr/bin/env python3
"""CSV to JSON conversion module."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file data to JSON format and save to data.json."""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            reader = csv.DictReader(csv_f)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f)

        return True
    except Exception:
        return False
