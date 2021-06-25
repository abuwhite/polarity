#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of gendiff."""

from gendiff import cli, stylish


def main():
    """Скрипт запуска сравнения файлов."""
    args = cli.run()
    stylish.diff_print(*args)


if __name__ == '__main__':
    main()
