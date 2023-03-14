import json
import yaml
import os


def load_data(file_path):
    with open(file_path) as file:
        _, extension = os.path.splitext(file_path)
        if extension == '.json':
            return json.load(file)
        elif extension in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unknown file extension: {extension}")
