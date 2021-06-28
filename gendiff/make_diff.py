# -*- coding: utf-8 -*-

"""Module with the function gendiff."""

from gendiff.constants import FLAG, NAME, VALUE


def make_diffs(data1, data2):
    """Creating File Differences.

    Creates an intermediate representation
    difference between two files.

    Args:
        data1: The first data file.
        data2: The second data file.

    Returns:
        list: Data with an intermediate representation.
    """
    diffs = []

    for key in sorted(data1.keys() | data2.keys()):
        val1 = data1.get(key)
        val2 = data2.get(key)

        if isinstance(val1, dict) and isinstance(val2, dict):
            if val1 != val2:
                diffs.append({FLAG: 'is_dict', NAME: key, VALUE: make_diffs(val1, val2)})
        elif val1 == val2:
            diffs.append({FLAG: 'unchanged', NAME: key, VALUE: val1})
        elif key not in data2:
            diffs.append({FLAG: 'removed', NAME: key, VALUE: val1})
        elif key not in data1:
            diffs.append({FLAG: 'added', NAME: key, VALUE: val2})
        else:
            diffs.append({FLAG: 'changed_old', NAME: key, VALUE: val1})
            diffs.append({FLAG: 'changed_new', NAME: key, VALUE: val2})
    return diffs
