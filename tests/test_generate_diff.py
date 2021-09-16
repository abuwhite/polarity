# -*- coding: utf-8 -*-
"""Test make_diff.py"""

from diffepy import make_diffs
from diffepy.utils import stylish, plain, json
from diffepy.api.parser import get_dict

FIRST_JSON = 'tests/fixtures/file1.json'
SECOND_JSON = 'tests/fixtures/file2.json'
FIRST_YAML = 'tests/fixtures/file1.yml'
SECOND_YAML = 'tests/fixtures/file2.yml'

with open('tests/fixtures/result_stylish.txt', 'r') as file:
    stylish_correct = file.read()

with open('tests/fixtures/result_plain.txt', 'r') as file:
    plain_correct = file.read()

with open('tests/fixtures/result_json.txt', 'r') as file:
    json_correct = file.read()


def test_make_diffs_first():
    print('in test_make_diffs_second')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    assert isinstance(make_diffs(file1, file2), list)


def test_make_diffs_second():
    print('in test_make_diffs_second')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    assert isinstance(make_diffs(file1, file2), list)


def test_stylish_first():
    print('in test_stylish_second')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    data = make_diffs(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct


def test_stylish_second():
    print('in test_stylish_second')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    data = make_diffs(file1, file2)
    assert stylish.make_stylish(data) == stylish_correct


def test_plain_first():
    print('in test_plain_first')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    data = make_diffs(file1, file2)
    assert plain.make_plain(data) == plain_correct


def test_plain_second():
    print('in test_plain_second')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    data = make_diffs(file1, file2)
    assert plain.make_plain(data) == plain_correct


def test_json_first():
    print('in test_json_first')
    file1 = get_dict(FIRST_JSON)
    file2 = get_dict(SECOND_JSON)
    data = make_diffs(file1, file2)
    assert json.make_json(data) == json_correct


def test_json_second():
    print('in test_json_second')
    file1 = get_dict(FIRST_YAML)
    file2 = get_dict(SECOND_YAML)
    data = make_diffs(file1, file2)
    assert json.make_json(data) == json_correct
