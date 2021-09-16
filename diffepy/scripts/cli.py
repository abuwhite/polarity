# -*- coding: utf-8 -*-

"""Args."""

import argparse

from diffepy.api.gendiff import generate_diff


def get_args():
    """Возвращаем принятые аргументы.

    Returns:
        class: 'argparse.Namespace'
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def main():
    """Скрипт запуска сравнения файлов."""
    print(generate_diff(
        get_args().first_file,
        get_args().second_file,
        format_output=get_args().format
    ))


if __name__ == '__main__':
    main()
