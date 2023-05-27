import json
import yaml
import os
import argparse


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def parse_data(data, file_extension):
    if file_extension == '.json':
        return json.loads(data)
    elif file_extension in ['.yaml', '.yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unknown file extension: {file_extension}")


def load_data(file_path):
    _, extension = os.path.splitext(file_path)
    file_data = read_file(file_path)
    return parse_data(file_data, extension)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish')
    return parser.parse_args()
