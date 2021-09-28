# -*- coding: utf-8 -*-

"""Test make_diff.py"""

import os
import ast

from polarity import make_diffs
from polarity.utils import stylish, plain, json
from polarity.api.parser import get_dict

from polarity.api.difference import generate_diff


def get_fixture_path(name):
    return os.path.join('tests/fixtures', name)


first_json_filepath = get_fixture_path('file1.json')
second_json_filepath = get_fixture_path('file2.json')
first_yaml_filepath = get_fixture_path('file1.yml')
second_yaml_filepath = get_fixture_path('file2.yml')


with open('tests/fixtures/result_stylish.txt', 'r') as file:
    stylish_correct = file.read()

with open('tests/fixtures/result_plain.txt', 'r') as file:
    plain_correct = file.read()

with open('tests/fixtures/result_json.txt', 'r') as file:
    json_correct = file.read()

with open('tests/fixtures/result_json_dict_formatting.txt', 'r') as file:
    contents = file.read()
    dict_formatting_correct = ast.literal_eval(contents)


def test_make_diffs_first():
    print('in test_make_diffs_second')
    first_file = get_dict(first_json_filepath)
    second_file = get_dict(second_json_filepath)
    assert isinstance(make_diffs(first_file, second_file), list)


def test_make_diffs_second():
    print('in test_make_diffs_second')
    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    assert isinstance(make_diffs(first_file, second_file), list)


def test_stylish_first():
    print('in test_stylish_second')
    first_file = get_dict(first_json_filepath)
    second_file = get_dict(second_json_filepath)
    data = make_diffs(first_file, second_file)
    assert stylish.make_stylish(data) == stylish_correct


def test_stylish_second():
    print('in test_stylish_second')
    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    data = make_diffs(first_file, second_file)
    assert stylish.make_stylish(data) == stylish_correct


def test_plain_first():
    print('in test_plain_first')
    first_file = get_dict(first_json_filepath)
    second_file = get_dict(second_json_filepath)
    data = make_diffs(first_file, second_file)
    assert plain.make_plain(data) == plain_correct


def test_plain_second():
    print('in test_plain_second')
    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    data = make_diffs(first_file, second_file)
    assert plain.make_plain(data) == plain_correct


def test_make_json():
    print('in test_make_json')
    first_file = get_dict(first_json_filepath)
    second_file = get_dict(second_json_filepath)
    data = make_diffs(first_file, second_file)
    assert json.make_json(data) == json_correct


def test_dict_formatting():
    print('in test_dict_formatting')
    first_file = get_dict(first_json_filepath)
    second_file = get_dict(second_json_filepath)
    actual = json.dict_formatting(make_diffs(first_file, second_file))
    assert actual == dict_formatting_correct


def test_difference_stylish():
    print('in difference stylish')
    actual = generate_diff(
        first_json_filepath,
        second_json_filepath,
        format_output='stylish'
    )

    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    expect = stylish.make_stylish(make_diffs(first_file, second_file))
    assert actual == expect


def test_difference_plain():
    print('in difference plain')
    actual = generate_diff(
        first_json_filepath,
        second_json_filepath,
        format_output='plain'
    )

    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    expect = plain.make_plain(make_diffs(first_file, second_file))
    assert actual == expect


def test_difference_json():
    print('in difference json')
    actual = generate_diff(
        first_json_filepath,
        second_json_filepath,
        format_output='json'
    )

    first_file = get_dict(first_yaml_filepath)
    second_file = get_dict(second_yaml_filepath)
    expect = json.make_json(make_diffs(first_file, second_file))
    assert actual == expect
