# -*- coding: utf-8 -*-
"""Test make_diff.py"""

from gendiff import make_diffs_representation
from gendiff.formatters import stylish, plain
from gendiff.parser import get_dict

BEFORE_PATH = 'tests/fixtures/file1.json'
AFTER_PATH = 'tests/fixtures/file2.json'

with open('tests/fixtures/result_stylish.txt', 'r') as file:
    stylish_correct = file.read()

with open('tests/fixtures/result_plain.txt', 'r') as file:
    plain_correct = file.read()


def test_make_diffs():
    print('in test_make_diffs')
    file1 = get_dict(BEFORE_PATH)
    file2 = get_dict(AFTER_PATH)
    assert isinstance(make_diffs_representation(file1, file2), list)


def test_stylish():
    print('in test_stylish')
    file1 = get_dict(BEFORE_PATH)
    file2 = get_dict(AFTER_PATH)
    data = make_diffs_representation(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct


def test_plain():
    print('in test_plain')
    file1 = get_dict(BEFORE_PATH)
    file2 = get_dict(AFTER_PATH)
    data = make_diffs_representation(file1, file2)
    print(plain.make_plain(data))
    assert plain.make_plain(data) == plain_correct
