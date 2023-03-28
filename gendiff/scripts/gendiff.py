#!/usr/bin/env python3

import argparse

from gendiff.compare_data import compare_data
from gendiff.formatters.stylish import format_diff
from gendiff.parser import load_data


def generate_diff(file_path1, file_path2, format_='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = compare_data(data1, data2)
    if format_ == 'stylish':
        return format_diff(diff)
    else:
        raise ValueError(f"Unknown output format: {format_}")


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    args = parser.parse_args()

    if args.format not in ['stylish', 'plain', 'json']:
        raise ValueError(f"Unknown output format: {args.format}")

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
