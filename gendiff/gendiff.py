from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import make_json
from gendiff.parser import parse
from os.path import splitext


def generate_diff(path1, path2, formatter='stylish'):
    match formatter:
        case 'plain':
            formatter = plain
        case 'stylish':
            formatter = stylish
        case 'json':
            formatter = make_json
    data1 = get_file_content(path1)
    data2 = get_file_content(path2)
    sorted_diff = make_diff_tree(data1, data2)
    diff_strings = formatter(sorted_diff)
    return diff_strings


def get_file_content(path):
    with open(path) as file:
        file_extension = splitext(path)[1]
        return parse(file, file_extension)


def make_diff_tree(tree1, tree2):
    keys = sorted({*tree1.keys(), *tree2.keys()})
    diff_tree = []
    for key in keys:
        value1 = tree1.get(key)
        value2 = tree2.get(key)
        if key not in tree2:
            diff_tree.append(['removed', key, value1])
        elif key not in tree1:
            diff_tree.append(['added', key, value2])
        elif value1 == value2:
            diff_tree.append(['unchanged', key, value1])
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff_tree.append(['nested', key, make_diff_tree(value1, value2)])
        else:
            diff_tree.append(['changed', key, value1, value2])
    return diff_tree
