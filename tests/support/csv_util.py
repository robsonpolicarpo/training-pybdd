import csv
import logging
from typing import List


def write_csv(filepath: str, data: List[dict], has_header: bool = True):
    header = data[0].keys()
    with open(filepath, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, header)
        if has_header:
            writer.writeheader()
        writer.writerows(data)


def write_csv_str(filepath: str, data: List[str]):
    with open(filepath, 'w') as csv_file:
        for line in data:
            csv_file.write(line)
            csv_file.write('\n')


def read_like_dict(filepath: str, delimiter=';'):
    with open(filepath, mode='r', encoding='iso-8859-1') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows


def read(filepath: str, delimiter=';'):
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                logging.info(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                logging.info(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        logging.info(f'Processed {line_count} lines.')
