#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of gendiff."""

from gendiff import cli
from gendiff.utils import generate_diff


def main():
    """Скрипт запуска сравнения файлов."""
    cli.run(generate_diff.check_diff)


if __name__ == '__main__':
    main()
