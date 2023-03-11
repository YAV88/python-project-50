#!/usr/bin/env python3

import json
import argparse


def generate_diff(file_path1, file_path2):
    diff = {}
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in keys:
        if key not in data1:
            diff[f'+ {key}'] = data2[key]
        elif key not in data2:
            diff[f'- {key}'] = data1[key]
        elif data1[key] != data2[key]:
            diff[f'- {key}'] = data1[key]
            diff[f'+ {key}'] = data2[key]
        else:
            diff[f'  {key}'] = data1[key]

    return json.dumps(diff, indent=2)


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
