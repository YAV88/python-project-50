import pytest

from gendiff import generate_diff
from gendiff.parser import load_data
from gendiff.get_diff import get_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain


@pytest.fixture()
def file_path1():
    return "tests/fixtures/file1.json"


@pytest.fixture()
def file_path2():
    return "tests/fixtures/file2.json"


@pytest.fixture()
def file_path3():
    return "tests/fixtures/file3.json"


@pytest.fixture()
def file_path4():
    return "tests/fixtures/file4.json"


@pytest.fixture()
def expected_result_stylish():
    with open("tests/fixtures/expected_result.txt") as f:
        return f.read()


@pytest.fixture()
def expected_result_plain():
    with open("tests/fixtures/expected_result_plain.txt") as f:
        return f.read()


@pytest.fixture()
def expected_result_json():
    with open("tests/fixtures/expected_result_json.txt") as f:
        return f.read()


@pytest.mark.parametrize(
    "file_path1, file_path2, format_, expected_result",
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "stylish", None),
        ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "plain", None),
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "json", None),
    ],
)
def test_generate_diff(file_path1, file_path2, format_, expected_result, expected_result_stylish, expected_result_plain,
                       expected_result_json):
    if format_ == "stylish":
        expected_result = expected_result_stylish
    elif format_ == "plain":
        expected_result = expected_result_plain
    elif format_ == "json":
        expected_result = expected_result_json

    diff = generate_diff(file_path1, file_path2, format_)
    assert diff == expected_result


def test_format_stylish(file_path1, file_path2, expected_result_stylish):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    assert format_stylish(diff) == expected_result_stylish


def test_format_plain(file_path3, file_path4, expected_result_plain):
    data1 = load_data(file_path3)
    data2 = load_data(file_path4)
    diff = get_diff(data1, data2)
    assert format_plain(diff) == expected_result_plain


def test_format_json(file_path1, file_path2, expected_result_json):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    assert format_json(diff) == expected_result_json
