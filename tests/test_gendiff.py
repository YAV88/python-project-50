import pytest
import json

from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.get_diff import get_diff
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain


@pytest.fixture()
def file1():
    with open("tests/fixtures/file1.json") as f:
        return json.load(f)


@pytest.fixture()
def file2():
    with open("tests/fixtures/file2.json") as f:
        return json.load(f)


@pytest.fixture()
def file3():
    with open("tests/fixtures/file3.json") as f:
        return json.load(f)


@pytest.fixture()
def file4():
    with open("tests/fixtures/file4.json") as f:
        return json.load(f)


@pytest.fixture()
def expected_result():
    with open("tests/fixtures/expected_result.txt") as f:
        return f.read()


@pytest.fixture()
def nested_structures_result():
    with open("tests/fixtures/nested_structures_result.txt") as f:
        return f.read()


@pytest.fixture()
def expected_result_plain():
    with open("tests/fixtures/expected_result_plain.txt") as f:
        return f.read()


@pytest.fixture()
def expected_result_json():
    with open("tests/fixtures/expected_result_json.txt") as f:
        return f.read()


def test_get_diff(file1, file2, expected_result):
    diff = get_diff(file1, file2)
    assert format_stylish(diff) == expected_result


def test_format_json(file1, file2, expected_result_json):
    diff = get_diff(file1, file2)
    assert format_json(diff) == expected_result_json


def test_format_plain(file3, file4, expected_result_plain):
    diff = get_diff(file3, file4)
    assert format_plain(diff) == expected_result_plain


def test_generate_diff_stylish(file1, file2, expected_result):
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert diff == expected_result


def test_generate_diff_plain(file3, file4, expected_result_plain):
    diff = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json", format_='plain')
    assert diff == expected_result_plain


def test_generate_diff_json(file1, file2, expected_result_json):
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", format_='json')
    assert diff == expected_result_json
