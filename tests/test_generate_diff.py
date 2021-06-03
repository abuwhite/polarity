# -*- coding: utf-8 -*-
"""Test gen_diff.py"""

from gendiff import generate_diff

BEFORE_PATH = 'tests/fixtures/plain1.json'
AFTER_PATH = 'tests/fixtures/plain2.json'


def test_type():
    print('in test_type')
    assert type(generate_diff(BEFORE_PATH, AFTER_PATH)) == str


def test_data():
    print('in test_data')
    with open('tests/fixtures/plain_files.txt') as file:
        correct_result = file.read()
    assert generate_diff(BEFORE_PATH, AFTER_PATH) == correct_result
