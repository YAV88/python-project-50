#!/usr/bin/env python3

import json
import argparse


def generate_diff(file_path1, file_path2, output_format='flat'):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff.append((' ', key, value1))
        elif key in data1 and key in data2:
            diff.append(('-', key, value1))
            diff.append(('+', key, value2))
        elif key in data1:
            diff.append(('-', key, value1))
        else:
            diff.append(('+', key, value2))

    if output_format == 'json':
        diff = [{'type': t, 'key': k, 'value': v} for t, k, v in diff]
        return json.dumps(diff, indent=2)
    else:
        lines = []
        for t, k, v in diff:
            if t == ' ':
                lines.append('    {}: {}'.format(k, v))
            elif t == '-':
                lines.append('-   {}: {}'.format(k, v))
            elif t == '+':
                lines.append('+   {}: {}'.format(k, v))
        return '{{\n{}\n}}'.format('\n'.join(lines))



def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()


if __name__ == '__main__':
    main()
