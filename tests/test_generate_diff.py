# -*- coding: utf-8 -*-
"""Test make_diff.py"""

from gendiff import make_diffs_representation
from gendiff.formatters import stylish
from gendiff.parser import get_dict

with open('tests/fixtures/correct_stylish.txt', 'r') as file:
    stylish_correct = file.read()

BEFORE_PATH = 'tests/fixtures/file1.json'
AFTER_PATH = 'tests/fixtures/file2.json'


def test_type():
    print('in test_type')
    file1 = get_dict(BEFORE_PATH)
    file2 = get_dict(AFTER_PATH)
    assert isinstance(make_diffs_representation(file1, file2), list)


def test_data():
    print('in test_data')
    file1 = get_dict(BEFORE_PATH)
    file2 = get_dict(AFTER_PATH)
    data = make_diffs_representation(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct
