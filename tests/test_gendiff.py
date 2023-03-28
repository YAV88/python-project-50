import os
import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.formatters.plain import format_diff_plain


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


def test_format_diff_plain():
    # Тестирование вывода plain формата для пустого словаря
    assert format_diff_plain({}) == ''

    # Тестирование вывода plain формата для словаря с одним узлом
    assert format_diff_plain({'key': 'value'}) == "Property 'key' was value"

    # Тестирование вывода plain формата для словаря с несколькими узлами
    assert format_diff_plain({
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }) == "Property 'key1' was value1\nProperty 'key2' was value2\nProperty 'key3' was value3"

    # Тестирование вывода plain формата для словаря со вложенными узлами
    assert format_diff_plain({
        'key1': 'value1',
        'key2': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }) == "Property 'key1' was value1\nProperty 'key2.key3' was value3\nProperty 'key2.key4' was value4"

    # Тестирование вывода plain формата для словаря с несколькими уровнями вложенности
    assert format_diff_plain({
        'key1': {
            'key2': {
                'key3': {
                    'key4': 'value4'
                }
            }
        }
    }) == "Property 'key1.key2.key3.key4' was value4"


def test_generate_diff():
    # Тестирование генерации diff в формате plain для файлов с одинаковым содержимым
    file_path1 = os.path.join(os.getcwd(), 'tests/fixtures/file1.json')
    file_path2 = os.path.join(os.getcwd(), 'tests/fixtures/file2.yml')
    expected_output = '''Property '- follow' was false
Property '  host' was hexlet.io
Property '- proxy' was 123.234.53.22
Property '- timeout' was 50
Property '+ timeout' was 20
Property '+ verbose' was true'''
    assert generate_diff(file_path1, file_path2, format_='plain') == expected_output
