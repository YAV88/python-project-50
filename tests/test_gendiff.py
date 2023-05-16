import pytest
import json
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
def expected_result_json():
    with open("tests/fixtures/expected_result_json.txt") as f:
        return f.read()


def test_get_diff(file1, file2, expected_result):
    diff = get_diff(file1, file2)
    assert format_stylish(diff) == expected_result


def test_format_stylish(file3, file4, nested_structures_result):
    diff = get_diff(file3, file4)
    assert format_stylish(diff) == '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_format_json(file1, file2, expected_result_json):
    diff = get_diff(file1, file2)
    assert format_json(diff) == expected_result_json


def test_format_plain(file1, file2):
    diff = get_diff(file1, file2)
    assert format_plain(diff) == """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From [complex value] to [complex value]
Property 'verbose' was added with value: true"""