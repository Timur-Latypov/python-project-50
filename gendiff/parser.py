import yaml
import json


def parse_files(path1, path2):
    if path1.endswith('.json'):
        file1 = json.load(open(path1))
    if path1.endswith('.yml') or path1.endswith('.yaml'):
        file1 = yaml.load(open(path1), Loader=yaml.CLoader)
    if path2.endswith('.json'):
        file2 = json.load(open(path2))
    if path2.endswith('.yml') or path2.endswith('.yaml'):
        file2 = yaml.load(open(path2), Loader=yaml.CLoader)
    return file1, file2

# print(parser('tests/fixtures/file1.json', 'tests/fixtures/file2.yml'))
