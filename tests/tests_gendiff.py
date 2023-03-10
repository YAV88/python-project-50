from gendiff.scripts.gendiff import generate_diff


diff = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
print(diff)


def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

    expected_result = '{\n + "timeout": 20,\n - "proxy": "123.234.53.22,\n ' \
                      '- "timeout": 50,\n + "verbose": true,\n "host": "hexlet.io"\n}'

    assert generate_diff(file_path1, file_path2) == expected_result
