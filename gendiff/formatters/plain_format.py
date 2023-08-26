def plain(diffs):
    acc = []
    return make_strings(diffs, acc)


def make_strings(diffs, acc):
    diff_strings = list(map(lambda diff: make_string(diff, acc), diffs))
    return '\n'.join(filter_unchanged_strings(diff_strings))


def filter_unchanged_strings(strings):
    return [string for string in strings if string is not None]


def make_string(diff, acc):
    templates = {
        'different_values': "Property '{0}' was updated. From {1} to {2}",
        'removed': "Property '{0}' was removed",
        'added': "Property '{0}' was added with value: {1}",
    }
    state, key, *childrens = diff
    match state:
        case 'different_values':
            value1, value2 = childrens
            value1 = normalize(value1)
            value2 = normalize(value2)
            string = templates[state]
            return string.format('.'.join(acc + [key]), value1, value2)
        case 'different_dict':
            return make_strings(*childrens, acc + [key])
        case 'removed':
            [value] = childrens
            return templates[state].format('.'.join(acc + [key]))
        case 'added':
            [value] = childrens
            value = normalize(value)
            string = templates[state]
            return string.format('.'.join(acc + [key]), value)


def normalize(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value
