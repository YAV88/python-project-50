import os
import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def expected_result():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_result.txt')
    with open(file_path) as f:
        return f.read().strip()


def test_generate_diff_json(expected_result):
    file_path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result


def test_generate_diff_yml(expected_result):
    file_path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
    file_path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')
    result = generate_diff(file_path1, file_path2)
    assert result == expected_result
