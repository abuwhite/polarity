# -*- coding: utf-8 -*-

"""This is import function scripts."""

import json


def make_json(diffs) -> str:
    """
    Formatting the difference representation to json
    :param:
        diffs: dict.
    :return:
        str.
    """
    formatted_dict = dict_formatting(diffs)
    json_output: str = json.dumps(formatted_dict, sort_keys=True, indent=4)
    if not formatted_dict:
        return '{\n}'
    return json_output


def dict_formatting(diffs, parent_name=None):
    result = {}
    for diff in diffs:
        name = diff.get('name')
        condition = diff.get('condition')
        value = diff.get('value')
        if parent_name is None:
            current_key = str(name)
        else:
            current_key = f"{parent_name}.{name}"
        if condition == 'is_dict':
            value = dict_formatting(value, parent_name=current_key)
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
        else:
            result[current_key] = {
                'condition': condition,
                'value': value,
            }
    return result
