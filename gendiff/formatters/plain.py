# -*- coding: utf-8 -*-

"""This is import function scripts."""


def make_plain(dicts):
    """Generate a plain format.

    Args:
        dicts: Dict.

    Returns:
        str: Plain format.
    """
    plaint_output = generate_plain_string(dicts)
    if plaint_output:
        return plaint_output[:-1]
    return '{\n}'


def generate_plain_string(diffs, parent_name=''):
    """Generate a plain string format.

    Args:
        diffs: Dict.
        parent_name: Keys.

    Returns:
        str: String plains.
    """
    plains: str = ''
    for diff in diffs:
        name = diff.get('name')
        condition = diff.get('status')
        meaning = diff.get('value')
        if parent_name:
            full_key = '{p}.{n}'.format(p=parent_name, n=name)
        else:
            full_key = name

        key_str = "Property '{key}' was".format(key=full_key)
        val_str = formatter(meaning)

        if condition == 'is_dict':
            plains += generate_plain_string(meaning, parent_name=full_key)
        elif condition == 'changed_old':
            plains += '{k} updated. From {v} to '.format(k=key_str, v=val_str)
        elif condition == 'changed_new':
            plains += '{v}\n'.format(v=val_str)
        elif condition == 'added':
            plains += '{b} added with value: {v}\n'.format(b=key_str, v=val_str)
        elif condition == 'removed':
            plains += '{base} removed\n'.format(base=key_str)
    return plains


def formatter(value_plain):
    """Generate value.

    Args:
        value_plain: Value.

    Returns:
        items: Values
    """
    if isinstance(value_plain, bool):
        return 'true' if value_plain else 'false'
    elif value_plain is None:
        return 'null'
    elif isinstance(value_plain, str):
        return "'{val}'".format(val=value_plain)
    elif isinstance(value_plain, (int, float, complex)):
        return str(value_plain)
    return '[complex value]'
