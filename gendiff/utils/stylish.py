# -*- coding: utf-8 -*-

"""This is import function scripts."""

from gendiff.api.constants import FLAGS, SPACE


def make_stylish(diffs_list, tier=0):
    """Generate a stylish format.

    Args:
        diffs_list: list.
        tier: Levels

    Returns:
        str: Plain format.
    """
    diffs: str = '{'
    pit: str = SPACE * tier

    for diff in diffs_list:
        diffs = '{a}{b}'.format(a=diffs, b='\n')
        name = diff.get('name')
        condition = diff.get('status')
        s_val = diff.get('value')
        flag = FLAGS.get(condition)

        if condition == 'is_dict':
            diffs += '{i}  {f}  {n}: '.format(i=pit, f=flag, n=name)
            diffs += make_stylish(s_val, tier + 1)
        else:
            f_val = formatter(s_val, pit + SPACE)
            diffs += '{i}  {f} {n}: {v}'.format(i=pit, f=flag, n=name, v=f_val)
    diffs += '{n}{i}}}'.format(n='\n', i=pit)
    return diffs


def formatter(diff_val, pit):
    """Generate a formatter.

    Args:
        diff_val: list.
        pit: Levels

    Returns:
        str: Formatter.
    """
    if isinstance(diff_val, bool):
        return 'true' if diff_val else 'false'
    if diff_val is None:
        return 'null'
    if isinstance(diff_val, dict):
        string = '{\n'
        for key, second in diff_val.items():
            string += '{s}{i}{k}: '.format(s=SPACE, i=pit, k=key)
            string += formatter(second, pit=pit + SPACE)
            string += '{n}'.format(n='\n')
        string += '{i}}}'.format(i=pit)
        return string
    return str(diff_val)
