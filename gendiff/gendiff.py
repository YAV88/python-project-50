from gendiff.get_diff import get_diff
from gendiff.parser import load_data
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def generate_diff(file_path1, file_path2, format_='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    if format_ == 'plain':
        return format_plain(diff)
    elif format_ == 'json':
        return format_json(diff)
    else:
        return format_stylish(diff)
