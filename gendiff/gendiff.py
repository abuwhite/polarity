#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of gendiff."""

from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.make_diff import make_diffs
from gendiff.parser import get_dict


def generate_diff(first_file, second_file, format_output='stylish'):
    """Get the difference of the files.

    Args:
        first_file: First
        second_file: Second
        format_output: Format

    Returns:
        str: Generated output.
    """
    dict1 = get_dict(first_file)
    dict2 = get_dict(second_file)
    diff = make_diffs(dict1, dict2)
    if format_output == 'plain':
        return make_plain(diff)
    elif format_output == 'json':
        return make_json(diff)
    return make_stylish(diff)
