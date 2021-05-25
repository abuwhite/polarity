#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test generate_diff.py"""

from gendiff import get_diff

FIRST_TEST_FILE = 'tests/test_file1.json'
SECOND_TEST_FILE = 'tests/test_file2.json'
CORRECT_RESULT = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'


def test_tree():
    print('in test_tree')
    assert get_diff(FIRST_TEST_FILE, SECOND_TEST_FILE) == CORRECT_RESULT


def test_type():
    print('in test_type')
    assert type(get_diff(FIRST_TEST_FILE, SECOND_TEST_FILE)) == str
