# -*- coding: utf-8 -*-

"""This is import function scripts."""

from gendiff.constants import SPACE, FLAGS
from gendiff.make_diff import get_value, get_name, get_condition


def make_plain(items):
    plaint_output = generate_plain_string(items)
    if plaint_output:
        return plaint_output[:-1]
    else:
        return '{\n}'


def generate_plain_string(diffs, parent_name=''):
    result: str = ''
    for diff in diffs:
        name = diff.get('name')
        condition = diff.get('status')
        value = diff.get('value')
        if parent_name:
            key_full_path = f"{parent_name}.{name}"
        else:
            key_full_path = name

        base_string = f"Property '{key_full_path}' was"
        value_string = formatter(value)

        if condition == 'is_dict':
            result += generate_plain_string(value, parent_name=key_full_path)
        elif condition == 'changed_old':
            result += f"{base_string} updated. From {value_string} to "
        elif condition == 'changed_new':
            result += f"{value_string}\n"
        elif condition == 'added':
            result += f"{base_string} added with value: {value_string}\n"
        elif condition == 'removed':
            result += f"{base_string} removed\n"
        else:
            pass
    return result


def formatter(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return "'{val}'".format(val=value)
    if isinstance(value, (int, float, complex)):
        return str(value)
    return "[complex value]"
