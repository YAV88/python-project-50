#!/usr/bin/env python3

import argparse
import json
from collections import defaultdict


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = defaultdict(dict)

    for key in data1.keys() | data2.keys():
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key][" "] = data1[key]
            else:
                diff[key]["-"] = data1[key]
                diff[key]["+"] = data2[key]
        elif key in data1:
            diff[key]["-"] = data1[key]
        else:
            diff[key]["+"] = data2[key]

    diff_lines = []
    for key, values in sorted(diff.items()):
        for symbol, value in values.items():
            if isinstance(value, bool):
                value = str(value).lower()
            if isinstance(value, str):
                value = f'{value}'
            diff_lines.append(f'  {symbol} {key}: {value}')

    return '{\n' + '\n'.join(diff_lines) + '\n}'


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

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
