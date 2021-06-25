# -*- coding: utf-8 -*-

"""Module with the function gendiff."""

from gendiff.constants import FLAG


def generate_diff(data1, data2):
    result = []

    for key in sorted(data1.keys() | data2.keys()):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            if value1 != value2:
                result.append({FLAG: 'is_dict', 'name': key, 'children': generate_diff(value1, value2)})
        elif value1 == value2:
            result.append({FLAG: 'unchanged', 'name': key, 'value': value1})
        elif key not in data2:
            result.append({FLAG: 'removed', 'name': key, 'value': value1})
        elif key not in data1:
            result.append({FLAG: 'added', 'name': key, 'value': value2})
        else:
            result.append({FLAG: 'changed_old', 'name': key, 'value': value1})
            result.append({FLAG: 'changed_new', 'name': key, 'value': value2})
    return result
