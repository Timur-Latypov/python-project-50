def stylish(diffs):
    return make_strings(diffs) + '\n}'


def make_strings(diffs, depth=1):
    diff_strings = list(map(lambda diff: make_string(diff, depth), diffs))
    return ('{\n' + '\n'.join(diff_strings))


def make_string(diff, depth):
    state, key, *childrens = diff
    indent = ' ' * (depth * 4 - 2)
    match state:
        case 'unchanged':
            [value] = childrens
            return f'{indent}  {key}: {normalize(value, depth)}'
        case 'changed':
            value1, value2 = childrens
            return f'{indent}- {key}: {normalize(value1, depth)}\n'\
                + f'{indent}+ {key}: {normalize(value2, depth)}'
        case 'nested':
            strings = make_strings(*childrens, depth + 1)
            return f'{indent}  {key}: {strings}' + f'\n{indent}  }}'
        case 'removed':
            [value] = childrens
            return f'{indent}- {key}: {normalize(value, depth)}'
        case 'added':
            [value] = childrens
            return f'{indent}+ {key}: {normalize(value, depth)}'


def normalize(item, depth):
    if isinstance(item, dict):
        return dict_to_string(item, depth)
    elif item is True or item is False:
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return item


def dict_to_string(dictionary, depth):
    indent = ' ' * (depth * 4 - 2)
    strings = [f'{indent}  {key}: {normalize(value, depth + 1)}'
               for key, value in dictionary.items()]
    return '{\n    ' + '\n    '.join(strings) + f'\n{indent}  }}'
