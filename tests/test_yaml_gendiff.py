# -*- coding: utf-8 -*-
"""Test generate_diff.py"""

from gendiff.utils import generate_diff

FIRST_TEST_FILE = 'tests/fixtures/test_file1.yml'
SECOND_TEST_FILE = 'tests/fixtures/test_file2.yml'
CORRECT_RESULT = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'


def test_type():
    print('in test_type')
    assert type(generate_diff.check_diff(FIRST_TEST_FILE, SECOND_TEST_FILE)) == str


def test_data():
    print('in test_data')
    assert generate_diff.check_diff(FIRST_TEST_FILE, SECOND_TEST_FILE) == CORRECT_RESULT
