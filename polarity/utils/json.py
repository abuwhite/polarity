# -*- coding: utf-8 -*-

"""This is import function scripts."""

import json


def make_json(diffs) -> str:
    """Form an intermediate json representation.

    Args:
        diffs: String.

    Returns:
        json_output(str): Json output
    """
    formatted_dict = dict_formatting(diffs)

    json_output: str = json.dumps(formatted_dict, sort_keys=True, indent=4)
    if not formatted_dict:
        return "{\n}"
    return json_output


def dict_formatting(diffs, parent_name=None):
    """Create a dictionary.

    Args:
        diffs: Dict.
        parent_name: None

    Returns:
        result(dict): Dict output
    """
    diffs_dict = {}
    for diff in diffs:
        name = diff.get("name")
        condition = diff.get("condition")
        diff_value = diff.get("value")
        if parent_name is None:
            current_key = str(name)
        else:
            current_key = "{p}.{n}".format(p=parent_name, n=name)
        if condition == "is_dict":
            value_dict = dict_formatting(diff_value, parent_name=current_key)
            diffs_dict[current_key] = {
                "condition": condition,
                "value": value_dict,
            }
        else:
            diffs_dict[current_key] = {
                "condition": condition,
                "value": diff_value,
            }
    return diffs_dict
