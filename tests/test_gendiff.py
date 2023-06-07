import pytest
from gendiff import generate_diff
from gendiff.parser import load_data
from gendiff.get_diff import get_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain


@pytest.mark.parametrize(
    "file_path1, file_path2, file_path3, file_path4, format_, expected_result",
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", None, None, "stylish", "tests/fixtures/expected_result.txt"),
        (None, None, "tests/fixtures/file3.json", "tests/fixtures/file4.json", "plain", "tests/fixtures/expected_result_plain.txt"),
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json", None, None, "json", "tests/fixtures/expected_result_json.txt"),
    ],
)
def test_generate_diff(file_path1, file_path2, file_path3, file_path4, format_, expected_result):
    with open(expected_result) as f:
        expected_result_content = f.read()

    if format_ == "stylish":
        diff = generate_diff(file_path1, file_path2, format_)
    elif format_ == "plain":
        diff = generate_diff(file_path3, file_path4, format_)
    elif format_ == "json":
        diff = generate_diff(file_path1, file_path2, format_)

    assert diff == expected_result_content


@pytest.mark.parametrize(
    "file_path1, file_path2, file_path3, file_path4, format_",
    [
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
         "tests/fixtures/file3.json", "tests/fixtures/file4.json", "stylish"),
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
         "tests/fixtures/file3.json", "tests/fixtures/file4.json", "plain"),
        ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
         "tests/fixtures/file3.json", "tests/fixtures/file4.json", "json"),
    ],
)
def test_format(file_path1, file_path2, file_path3, file_path4, format_):
    if format_ == "stylish":
        data1 = load_data(file_path1)
        data2 = load_data(file_path2)
        diff = get_diff(data1, data2)
        expected_result_file = "tests/fixtures/expected_result.txt"
        with open(expected_result_file) as f:
            expected_result_content = f.read()
        assert format_stylish(diff) == expected_result_content
    elif format_ == "plain":
        data1 = load_data(file_path3)
        data2 = load_data(file_path4)
        diff = get_diff(data1, data2)
        expected_result_file = "tests/fixtures/expected_result_plain.txt"
        with open(expected_result_file) as f:
            expected_result_content = f.read()
        assert format_plain(diff) == expected_result_content
    elif format_ == "json":
        data1 = load_data(file_path1)
        data2 = load_data(file_path2)
        diff = get_diff(data1, data2)
        expected_result_file = "tests/fixtures/expected_result_json.txt"
        with open(expected_result_file) as f:
            expected_result_content = f.read()
        assert format_json(diff) == expected_result_content
