# -*- coding: utf-8 -*-

"""Parser."""

import json
import os
import yaml


def read_file(path):
    """Открываем и возвращаем данные из файла.

    Args:
        path: Абсолютный или относительный адрес файла.

    Returns:
        set: Возвращаем данные из файла.
    """
    full_name = os.path.basename(path)
    name = os.path.splitext(full_name)[1]

    if name == '.json':
        with open(path) as file_json:
            return json.load(file_json)
    elif name in {'.yml', '.yaml'}:
        with open(path) as file_yaml:
            return yaml.safe_load(file_yaml)
    else:
        print('Oops, you can only process JSON or YAML files.')
