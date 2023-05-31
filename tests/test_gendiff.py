import pytest

from gendiff import generate_diff
from gendiff.parser import load_data
from gendiff.get_diff import get_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain


@pytest.fixture
def file_paths():
    return [
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
        "tests/fixtures/file3.json",
        "tests/fixtures/file4.json",
    ]


@pytest.fixture
def expected_results_stylish():
    with open("tests/fixtures/expected_result.txt") as f:
        stylish_result = f.read()
    with open("tests/fixtures/expected_result_plain.txt") as f:
        plain_result = f.read()
    with open("tests/fixtures/expected_result_json.txt") as f:
        json_result = f.read()
    return [stylish_result, plain_result, json_result]


@pytest.mark.parametrize(
    "file_path1, file_path2, format_, expected_result",
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "stylish", None),
        ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "plain", None),
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "json", None),
    ],
)
def test_generate_diff(
    file_path1, file_path2, format_, expected_result, expected_results_stylish
):
    expected_result = (
        expected_results_stylish[0]
        if format_ == "stylish"
        else expected_results_stylish[1]
        if format_ == "plain"
        else expected_results_stylish[2]
    )

    diff = generate_diff(file_path1, file_path2, format_)
    assert diff == expected_result


def test_format_stylish(file_paths, expected_results_stylish):
    file_path1, file_path2, _, _ = file_paths
    expected_result_stylish, _, _ = expected_results_stylish

    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    assert format_stylish(diff) == expected_result_stylish


def test_format_plain(file_paths, expected_results_stylish):
    _, _, file_path3, file_path4 = file_paths
    _, expected_result_plain, _ = expected_results_stylish

    data1 = load_data(file_path3)
    data2 = load_data(file_path4)
    diff = get_diff(data1, data2)
    assert format_plain(diff) == expected_result_plain


def test_format_json(file_paths, expected_results_stylish):
    file_path1, file_path2, _, _ = file_paths
    _, _, expected_result_json = expected_results_stylish

    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = get_diff(data1, data2)
    assert format_json(diff) == expected_result_json
