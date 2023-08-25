def plain(diffs):
    templates = {
        'different_values': "Property '{0}' was updated. From {1} to {2}",
        'removed': "Property '{0}' was removed",
        'added': "Property '{0}' was added with value: {1}",
    }

    def inner(diffs, acc):
        def walk(diff):
            state, _, key, *childrens = diff
            match state:
                case 'different_values':
                    value1, value2 = childrens
                    value1 = normalize(value1)
                    value2 = normalize(value2)
                    string = templates[state]
                    return string.format('.'.join(acc + [key]), value1, value2)
                # f"Property '{'.'.join(acc + [key])}'" + \
        # f" was updated. From {normalize(value1)} to {normalize(value2)}"
                case 'different_dict':
                    return inner(*childrens, acc + [key])
                case 'removed':
                    [value] = childrens
                    return templates[state].format('.'.join(acc + [key]))
                case 'added':
                    [value] = childrens
                    value = normalize(value)
                    string = templates[state]
                    return string.format('.'.join(acc + [key]), value)

        diff_strings = list(filter(
            lambda item: item is not None, map(walk, diffs)))
        return '\n'.join(diff_strings)
    acc = []
    return inner(diffs, acc)


'''def to_string(*args):
    state, args = args
    match state:
        case 'different_values':
            acc, value1, value2 = args
            return f"Property '{'.'.join(acc + [key])}' was updated.
              From {normalize(value1)} to {normalize(value2)}"
'''


def normalize(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"
