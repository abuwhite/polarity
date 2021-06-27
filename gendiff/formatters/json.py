# -*- coding: utf-8 -*-

"""This is import function scripts."""

from gendiff.constants import SPACE, FLAGS


def make_json(items, tier=0):
    result: str = '{'
    indent: str = SPACE * tier

    for item in items:
        result += '\n'
        name = item.get('name')
        condition = item.get('status')
        value = item.get('value')

        if condition == 'is_dict':
            result += '{ind}  "{nme}": '.format(ind=indent, nme=name)
            result += make_json(value, tier + 1)
        else:
            value = formatter(value, indent + SPACE)
            result += '{ind}  "{nme}": {val}'.format(ind=indent, nme=name, val=value)
    result += f'\n{indent}}}'
    return result


def formatter(value, indent):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return '"{}"'.format(value)
    if value is None:
        return "null"
    if isinstance(value, dict):
        string = "{\n"
        for key, value in value.items():
            string += '{s}{i}"{k}": '.format(s=SPACE, i=indent, k=key)
            string += f"{formatter(value, indent + SPACE)}"
            string += "\n"
        string += f"{indent}}}"
        return string
    return value
