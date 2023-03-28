import os
import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.formatters.stylish import format_diff
from gendiff.compare_data import compare_data


@pytest.fixture
def expected_result():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_result.txt')
    with open(file_path) as f:
        return f.read().strip()


@pytest.fixture
def nested_structures_result():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_structures_result.txt')
    with open(file_path) as n:
        return n.read().strip()


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


def test_generate_diff_yaml_nested(expected_result):
    file_path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file3.yaml')
    file_path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file4.yaml')
    result = generate_diff(file_path1, file_path2)
    expected_result_yaml = """{
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
}"""

    assert result == expected_result_yaml



