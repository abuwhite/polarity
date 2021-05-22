#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gendiff import parser


def get_diff(file_path1, file_path2):
    print(file_path1)
    json1 = parser.read_file(file_path1)
    json2 = parser.read_file(file_path2)
    keys_json1 = sorted(list(json1.keys()))
    list_str = []

    for key in keys_json1:
        if json2.get(key) == json1.get(key):
            string = '   {}: {}'.format(key, json1.get(key))
            list_str.append(string)
            json2.pop(key)
        elif json2.get(key) is None:
            string = ' - {}: {}'.format(key, json1.get(key))
            list_str.append(string)
        else:
            string = ' - {}: {}'.format(key, json1.get(key))
            list_str.append(string)
            string = ' + {}: {}'.format(key, json2.get(key))
            list_str.append(string)
            json2.pop(key)

    keys_json2 = sorted(list(json2))
    for key in keys_json2:
        string = ' + {}: {}'.format(key, json2.get(key))
        list_str.append(string)

    result: str = '{\n' + '\n'.join(list_str) + '\n}'
    return result


def output(args):
    print(get_diff(args.first_file, args.second_file))