from gendiff.scripts.gendiff import generate_diff


diff = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
print(diff)
