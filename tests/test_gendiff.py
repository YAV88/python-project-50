import pytest
import json
from gendiff.scripts.gendiff import generate_diff


expected_result_json = open('./tests/fixtures/expected_result.txt', 'r')
result_json = expected_result_json.read()


def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == \
           '{\n  "- follow": false,\n  "  host": "hexlet.io",\n  "- proxy": "123.234.53.22",\n  "- timeout": 50,\n  "' \
           '+ timeout": 20,\n  "+ verbose": true\n}'

