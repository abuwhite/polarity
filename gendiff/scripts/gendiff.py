#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of gendiff."""

from gendiff import cli
from gendiff.utils import gen_diff


def main():
    """Скрипт запуска сравнения файлов."""
    cli.run(gen_diff.diff_print)


if __name__ == '__main__':
    main()
