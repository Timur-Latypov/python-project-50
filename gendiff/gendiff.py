from gendiff.formatters.stylish_format import stylish
from gendiff.parser import parse_files



def generate_diff(path1, path2, formatter=stylish): # noqa: ignore=C901
    file1, file2 = parse_files(path1, path2)

    def inner(tree1, tree2, depth=1):
        def walk(key, tree1, tree2):
            value1 = tree1.get(key)
            value2 = tree2.get(key)
            if key in tree1:
                if key in tree2:
                    if value1 == value2:
                        return ['equal', depth, key, value1]
                    elif isinstance(value1, dict) and isinstance(value2, dict):
                        return ['different_dict', depth, key,
                                inner(value1, value2, depth+1)]
                    else:
                        return ['different_values', depth, key, value1, value2]
                else:
                    return ['removed', depth, key, value1]
            else:
                return ['added', depth, key, value2]
        keys = sorted({*tree1.keys(), *tree2.keys()})
        diff = list(map(lambda key: walk(key, tree1, tree2), keys))
        return diff
    sorted_diff = inner(file1, file2)
    strings = formatter(sorted_diff)
    return strings

# f1 = "/media/timur/Windows/Hexlet Projects/Project 2
# /python-project-50/tests/fixtures/nested1.json"
# f2 = '/media/timur/Windows/Hexlet Projects/Project 2
# /python-project-50/tests/fixtures/nested2.json'
# f1 = "/media/timur/Windows/Hexlet Projects/Project
#  2/python-project-50/tests/fixtures/plain1.json"
# f2 = '/media/timur/Windows/Hexlet Projects/Project
#  2/python-project-50/tests/fixtures/plain2.json'

# print(generate_diff(f1, f2, plain))
