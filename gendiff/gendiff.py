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
    sorted_diff = make_diff(data1, data2)
    diff_strings = formatter(sorted_diff)
    return diff_strings


def get_file_content(path):
    with open(path) as file:
        file_extension = splitext(path)[1]
        return parse(file, file_extension)


def make_diff(tree1, tree2):
    keys = sorted({*tree1.keys(), *tree2.keys()})
    diff = list(map(lambda key: make_children(key, tree1, tree2), keys))
    return diff


def make_children(key, tree1, tree2):
    value1 = tree1.get(key)
    value2 = tree2.get(key)
    if key in tree1:
        if key in tree2:
            return compare_values(value1, value2, key)
        else:
            return ['removed', key, value1]
    else:
        return ['added', key, value2]


def compare_values(value1, value2, key):
    if value1 == value2:
        return ['equal', key, value1]
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return ['different_dict', key,
                make_diff(value1, value2)]
    else:
        return ['different_values', key, value1, value2]
