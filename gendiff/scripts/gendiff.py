#!/usr/bin/env python3

import argparse

from gendiff.compare_data import compare_data
from gendiff.formatters.stylish import format_diff_stylish
from gendiff.parser import load_data
from gendiff.formatters.plain import format_diff_plain


def generate_diff(file_path1, file_path2, format_='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = compare_data(data1, data2)
    if format_ == 'plain':
        return format_diff_plain(diff)
    elif format_ == 'json':
        return format_diff_json(diff)
    else:
        return format_diff_stylish(diff)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
