import json
import yaml
import os
import argparse


def load_data(file_path):
    with open(file_path) as file:
        _, extension = os.path.splitext(file_path)
        if extension == '.json':
            return json.load(file)
        elif extension in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unknown file extension: {extension}")


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
