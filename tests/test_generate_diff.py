# -*- coding: utf-8 -*-
"""Test gen_diff.py"""

from gendiff import generate_diff, stylish
from gendiff.parser import read_file

with open('tests/fixtures/correct_stylish.txt', 'r') as file:
    stylish_correct = file.read()

BEFORE_PATH = 'tests/fixtures/file1.json'
AFTER_PATH = 'tests/fixtures/file2.json'


def test_type():
    print('in test_type')
    file1 = read_file(BEFORE_PATH)
    file2 = read_file(AFTER_PATH)
    assert isinstance(generate_diff(file1, file2), list)


def test_data():
    print('in test_data')
    file1 = read_file(BEFORE_PATH)
    file2 = read_file(AFTER_PATH)
    data = generate_diff(file1, file2)
    print(stylish_correct)
    print(stylish.make_stylish(data))
    assert stylish.make_stylish(data) == stylish_correct
