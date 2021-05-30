# -*- coding: utf-8 -*-

"""Module with the function gendiff."""
from gendiff.utils import parser


def generate_diff(json1, json2):
    """Открываем и сравниваем два json файла.
    Args:
        json1: Первый файл
        json2: Второй файл
    Returns:
          str: Результат
    """
    list_str = []

    file1 = parser.read_file(json1)
    file2 = parser.read_file(json2)

    for key1 in sorted(file1):
        first_value = file1.get(key1)

        if file2.get(key1) == first_value:
            list_str.append('   {k}: {v}'.format(k=key1, v=first_value))
            file2.pop(key1)
        elif file2.get(key1) is None:
            list_str.append(' - {k}: {v}'.format(k=key1, v=first_value))
        else:
            list_str.append(' - {k}: {v}'.format(k=key1, v=first_value))
            list_str.append(' + {k}: {v}'.format(k=key1, v=file2.get(key1)))
            file2.pop(key1)

    for key2 in sorted(file2):
        list_str.append(' + {k}: {v}'.format(k=key2, v=file2.get(key2)))

    return '{o}{data}{c}'.format(o='{\n', data='\n'.join(list_str), c='\n}')


def diff_print(*args):
    print(generate_diff(*args))