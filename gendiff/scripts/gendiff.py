#!/usr/bin/python3

import argparse
import json
import os

first_file = json.load(open('/home/notabu/PycharmProjects/python-project-lvl2/hexlet_code/file1.json'))
second_file = json.load(open('/home/notabu/PycharmProjects/python-project-lvl2/hexlet_code/file2.json'))


def get_diff(file_path1, file_path2):
    keys_json1 = sorted(list(file_path1.keys()))
    list_str = []

    for key in keys_json1:
        if file_path2.get(key) == file_path1.get(key):
            string = '   {}: {}'.format(key, file_path1.get(key))
            list_str.append(string)
            file_path2.pop(key)
        elif file_path2.get(key) is None:
            string = ' - {}: {}'.format(key, file_path1.get(key))
            list_str.append(string)
        else:
            string = ' - {}: {}'.format(key, file_path1.get(key))
            list_str.append(string)
            string = ' + {}: {}'.format(key, file_path2.get(key))
            list_str.append(string)
            file_path2.pop(key)

    keys_json2 = sorted(list(file_path2))
    for key in keys_json2:
        string = ' + {}: {}'.format(key, file_path2.get(key))
        list_str.append(string)

    result = '{\n' + '\n'.join(list_str) + '\n}'
    return result



# dirname = os.path.dirname(file1.json)
#     print(dirname)




def gendiff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    gendiff()


if __name__ == "__main__":
    main()
