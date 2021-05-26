# -*- coding: utf-8 -*-

"""Args."""

import argparse


def run(diff):
    """Возвращаем принятые аргументы.

    Args:
        diff: Функция сравнения.

    Returns:
        class: 'argparse.Namespace'
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return diff(args.first_file, args.second_file)
