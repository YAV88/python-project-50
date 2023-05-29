import json
import yaml
import os


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
