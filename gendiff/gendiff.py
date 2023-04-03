from gendiff.compare_data import compare_data
from gendiff.formatters.stylish import format_diff_stylish
from gendiff.parser import load_data
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.json import format_diff_json


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
