def stylish(diffs):
    def inner(diffs):
        def walk(diff):
            state, depth, key, *childrens = diff
            indent = ' ' * (depth * 4 - 2)
            match state:
                case 'equal':
                    [value] = childrens
                    return f'{indent}  {key}: {dict_to_strings(value, indent)}'
                case 'different_values':
                    value1, value2 = childrens
                    return \
                        f'{indent}- {key}: {dict_to_strings(value1, indent)}\n'\
                        + f'{indent}+ {key}: {dict_to_strings(value2, indent)}'
                case 'different_dict':
                    strings = inner(*childrens)
                    return f'{indent}  {key}: {strings}' + f'\n{indent}  }}'
                case 'removed':
                    [value] = childrens
                    return f'{indent}- {key}: {dict_to_strings(value, indent)}'
                case 'added':
                    [value] = childrens
                    return f'{indent}+ {key}: {dict_to_strings(value, indent)}'

        diff_strings = list(map(walk, diffs))
        return ('{\n' + '\n'.join(diff_strings))
    return inner(diffs) + '\n}'


def dict_to_strings(item, indent):
    if isinstance(item, dict):
        strings = [f'{indent}  {key}: {dict_to_strings(value, indent+"    ")}'
                   for key, value in item.items()]
        return '{\n    ' + '\n    '.join(strings) + f'\n{indent}  }}'
    elif item is True or item is False:
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return item
