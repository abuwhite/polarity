# -*- coding: utf-8 -*-
"""Test make_diff.py"""

from gendiff import make_diffs_representation
from gendiff.formatters import stylish, plain
from gendiff.parser import get_dict

FIRST_JSON = 'tests/fixtures/file1.json'
SECOND_JSON = 'tests/fixtures/file2.json'
FIRST_YAML = 'tests/fixtures/file1.yml'
SECOND_YAML = 'tests/fixtures/file2.yml'

with open('tests/fixtures/result_stylish.txt', 'r') as file:
    stylish_correct = file.read()

with open('tests/fixtures/result_plain.txt', 'r') as file:
    plain_correct = file.read()


def test_json_make_diffs():
    print('in test_yaml_make_diffs')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    assert isinstance(make_diffs_representation(file1, file2), list)


def test_yaml_make_diffs():
    print('in test_yaml_make_diffs')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    assert isinstance(make_diffs_representation(file1, file2), list)


def test_json_stylish():
    print('in test_yaml_stylish')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    data = make_diffs_representation(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct


def test_yaml_stylish():
    print('in test_yaml_stylish')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    data = make_diffs_representation(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct


def test_json_plain():
    print('in test_yaml_plain')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    data = make_diffs_representation(file1, file2)
    assert plain.make_plain(data) == plain_correct


def test_yaml_plain():
    print('in test_yaml_plain')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    data = make_diffs_representation(file1, file2)
    assert plain.make_plain(data) == plain_correct
