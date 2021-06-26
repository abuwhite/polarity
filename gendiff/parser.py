# -*- coding: utf-8 -*-

"""Parser."""

import json
import os
import yaml


def json_parse(file):
    data = json.loads(open(file, 'r').read())
    return data


def yaml_parse(file):
    data = yaml.safe_load(open(file, 'r').read())
    return data


def get_dict(path):
    """Открываем и возвращаем данные из файла.

    Args:
        path: Абсолютный или относительный адрес файла.

    Returns:
        set: Возвращаем данные из файла.
    """
    extension = os.path.splitext(path)[-1]
    if extension == '.json':
        return json_parse(path)
    elif extension in {'.yml', '.yaml'}:
        return yaml_parse(path)
    raise NotImplementedError(f"Unsupported file type {extension}")
