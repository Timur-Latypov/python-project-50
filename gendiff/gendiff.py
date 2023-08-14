import json


def generate_diff(path1, path2):
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))
    diff = {}
    keys = [*file1.keys(), *file2.keys()]
    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key in file1:
            if key in file2:
                if value1 == value2:
                    diff[key] = {'equal': value1}
                    # f'  {key}: {value1}'.lower()
                else:
                    diff[key] = {'different': (value1, value2)}
                    # f'- {key}: {value1}\n+ {key}: {value2}'.lower()
            else:
                diff[key] = {'value1': value1}
                # f'- {key}: {value1}'.lower()
        elif key in file2:
            diff[key] = diff[key] = {'value2': value2}
            # f'+ {key}: {value2}'.lower()
    sorted_diff = {key: diff[key] for key in sorted(diff)}
    return ('{\n' + '\n'.join(make_strings(sorted_diff)) + '\n}')


def make_strings(diff):
    diff_strings = []
    for key in diff.keys():
        diff_status = diff[key]
        for state in diff_status:
            match state:
                case 'equal':
                    diff_strings.append(f'  {key}: {diff_status[state]}'.lower())
                case 'different':
                    diff_strings.append(f'- {key}: {diff_status[state][0]}\n+ {key}: {diff_status[state][1]}'.lower())
                case 'value1':
                    diff_strings.append(f'- {key}: {diff_status[state]}'.lower())
                case 'value2':
                    diff_strings.append(f'- {key}: {diff_status[state]}'.lower())
    return diff_strings


'''f1 = '/media/timur/Windows/Hexlet Projects/Project 2/test_files/file1.json'
f2 = '/media/timur/Windows/Hexlet Projects/Project 2/test_files/file2.json'

print(generate_diff(f1, f2))'''
