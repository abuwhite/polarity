# -*- coding: utf-8 -*-

"""Parser."""

import json
import os

import yaml


def json_parse(filename):
    """Открываем и возвращаем данные из файла.

    Args:
        filename: Абсолютный или относительный адрес файла.

    Returns:
        str: Возвращаем данные из файла.
    """
    with open(filename, 'r') as file_obj:
        json_file = file_obj.read()
    return json.loads(json_file)


def yaml_parse(filename):
    """Открываем и возвращаем данные из файла.

    Args:
        filename: Абсолютный или относительный адрес файла.

    Returns:
        str: Возвращаем данные из файла.
    """
    with open(filename, 'r') as file_obj:
        yaml_file = file_obj.read()
    return yaml.safe_load(yaml_file)


def get_dict(filename):
    """Открываем и возвращаем данные из файла.

    Args:
        filename: Абсолютный или относительный адрес файла.

    Raises:
        NotImplementedError: Error log.

    Returns:
        str: Returning file data.
    """
    extension = os.path.splitext(filename)[-1]
    if extension == '.json':
        return json_parse(filename)
    elif extension in {'.yml', '.yaml'}:
        return yaml_parse(filename)
    raise NotImplementedError('Unsupported file type {ex}'.format(ex=extension))
