# -*- coding: utf-8 -*-

"""Module with the function gendiff."""

from gendiff.constants import DICT, ADDED, REMOVED, CHANGED, UNCHANGED
from gendiff.stylish import formatter


def generate_diff(file1, file2):
    data = []

    for key in sorted(file1.keys() | file2.keys()):
        value1 = file1.get(key)
        value2 = file2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            if value1 != value2:
                data.append({'condition': DICT, 'key': key, 'value': None, 'children': generate_diff(value1, value2)})
            data.append({'condition': DICT, 'key': key, 'value': value1, 'children': None})
        elif value1 == value2:
            data.append({'condition': UNCHANGED, 'key': key, 'value': value1, 'children': None})
        elif key in file1 and key not in file2:
            data.append({'condition': REMOVED, 'key': key, 'value': value1, 'children': None})
        elif key in file2 and key not in file1:
            data.append({'condition': ADDED, 'key': key, 'value': value2, 'children': None})
        else:
            data.append({'condition': CHANGED, 'key': key, 'value': [value1, value2], 'children': None})

    return data


def diff_print(*args):
    print(formatter(generate_diff(*args)))