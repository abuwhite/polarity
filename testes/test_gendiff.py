#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gendiff.generate_diff import get_diff


def test_type():
    assert type(get_diff('testes/test_file1.json', 'testes/test_file2.json')) == str
