# -*- coding: utf-8 -*-

"""This is import function scripts."""

from gendiff.constants import DICT, ADDED, REMOVED, CHANGED, UNCHANGED


def formatter(items):
    list = []

    for item in items:
        condition = item.get('condition')
        key = item.get('key')
        value = item.get('value')
        children = item.get('children')

        if condition is DICT:
            list.append('    {k}: {v}'.format(k=key, v=formatter(children)))
        elif condition is CHANGED:
            list.append('  - {k}: {v}'.format(k=key, v=value[0]))
            list.append('  + {k}: {v}'.format(k=key, v=value[1]))
        elif condition is UNCHANGED:
            list.append('    {k}: {v}'.format(k=key, v=value))
        elif condition is REMOVED:
            list.append('  - {k}: {v}'.format(k=key, v=value))
        elif condition is ADDED:
            list.append('  + {k}: {v}'.format(k=key, v=value))

    return '{o}{data}{c}'.format(o='{\n', data='\n'.join(list), c='\n}')