#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of gendiff."""

from gendiff.parser import get_dict
from gendiff.make_diff import make_diffs_representation
from gendiff.formatters.stylish import make_stylish


def generate_diff(first_file,
                  second_file,
                  format_output='stylish'):
    dict1 = get_dict(first_file)
    dict2 = get_dict(second_file)
    diff = make_diffs_representation(dict1, dict2)
    # if format_output == 'plain':
    #     return make_plain(diff)
    # elif format_output == 'json':
    #     return make_json(diff)
    return make_stylish(diff)
