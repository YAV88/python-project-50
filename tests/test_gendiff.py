import pytest
from gendiff import generate_diff
from gendiff.parser import load_data, parse_data
from gendiff.get_diff import get_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain


parameters = [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "stylish", "tests/fixtures/expected_result.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "plain", "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "json", "tests/fixtures/expected_result_json.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "stylish", "tests/fixtures/expected_result.txt"),
    ("tests/fixtures/file3.yaml", "tests/fixtures/file4.yaml", "plain", "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "json", "tests/fixtures/expected_result_json.txt")
]


@pytest.mark.parametrize("file_path1, file_path2, format_, expected_result", parameters)
def test_generate_diff(file_path1, file_path2, format_, expected_result):
    with open(expected_result) as f:
        expected_result_content = f.read()

    diff = generate_diff(file_path1, file_path2, format_)

    assert diff == expected_result_content


@pytest.mark.parametrize("file_path1, file_path2, format_, expected_result", parameters)
def test_get_diff(file_path1, file_path2, format_, expected_result):
    with open(expected_result) as f:
        expected_result_content = f.read()

    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    formatted_diff = ""

    if format_ == "stylish":
        formatted_diff = format_stylish(diff)
    elif format_ == "json":
        formatted_diff = format_json(diff)
    elif format_ == "plain":
        formatted_diff = format_plain(diff)

    assert formatted_diff == expected_result_content


@pytest.mark.parametrize(
    "data, data_format, expected_result",
    [
        ('{"key": "value"}', '.json', {"key": "value"}),
        ('key: value', '.yaml', {"key": "value"}),
        ('key: value', '.yml', {"key": "value"}),
        ('{"key": "value"}', '.txt', ValueError),
    ],
)
def test_parse_data(data, data_format, expected_result):
    if expected_result == ValueError:
        with pytest.raises(ValueError):
            parse_data(data, data_format)
    else:
        assert parse_data(data, data_format) == expected_result
