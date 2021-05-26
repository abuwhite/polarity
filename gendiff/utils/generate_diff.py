# -*- coding: utf-8 -*-

"""Module with the function gendiff."""

from gendiff.utils import parser


def check_diff(file_path1, file_path2):
    """Открываем и сравниваем два json файла.

    Args:
        file_path1: Первый файл
        file_path2: Второй файл
    """
    json1 = parser.read_file(file_path1)
    json2 = parser.read_file(file_path2)
    list_str = []

    for key1 in sorted(json1):
        first_value = json1.get(key1)

        if json2.get(key1) == first_value:
            list_str.append('   {k}: {v}'.format(k=key1, v=first_value))
            json2.pop(key1)
        elif json2.get(key1) is None:
            list_str.append(' - {k}: {v}'.format(k=key1, v=first_value))
        else:
            list_str.append(' - {k}: {v}'.format(k=key1, v=first_value))
            list_str.append(' + {k}: {v}'.format(k=key1, v=json2.get(key1)))
            json2.pop(key1)

    for key2 in sorted(json2):
        list_str.append(' + {k}: {v}'.format(k=key2, v=json2.get(key2)))

    return '{o}{data}{c}'.format(o='{\n', data='\n'.join(list_str), c='\n}')


def diff_print(*args):
    print(check_diff(*args))