# -*- coding: utf-8 -*-

"""Args."""

import argparse
from gendiff.parser import read_file


def run():
    """Возвращаем принятые аргументы.

    Returns:
        class: 'argparse.Namespace'
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = read_file(args.first_file)
    file2 = read_file(args.second_file)
    return file1, file2
