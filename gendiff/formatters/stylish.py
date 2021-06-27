# -*- coding: utf-8 -*-

"""This is import function scripts."""

from gendiff.constants import SPACE, FLAGS


def make_stylish(items, tier=0):
    result: str = '{'
    indent: str = SPACE * tier

    for item in items:
        result += '\n'
        name = item.get('name')
        condition = item.get('status')
        value = item.get('value')
        flag = FLAGS.get(condition)

        if condition == 'is_dict':
            result += f'{indent}  {flag}  {name}: '
            result += make_stylish(value, tier + 1)
        else:
            value = formatter(value, indent + SPACE)
            result += f'{indent}  {flag} {name}: {value}'
    result += f'\n{indent}}}'
    return result


def formatter(value, indent):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, dict):
        string = "{\n"
        for key, value in value.items():
            string += f"{SPACE}{indent}{key}: "
            string += formatter(value, indent=indent + SPACE)
            string += "\n"
        string += f"{indent}}}"
        return string
    return str(value)