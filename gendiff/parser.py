# -*- coding: utf-8 -*-

"""Parser."""

import json
import os

import yaml


def open_file(filename):
    """Open a file.

        Args:
            filename: Absolute or relative file address.

        Returns:
            str: Returning data from the file.
        """
    with open(filename, 'r') as file_obj:
        return file_obj.read()


def json_parse(json_dict):
    """Convert from JSON to python

    Args:
        json_dict: Absolute or relative file address.

    Returns:
        dict: Returns the python dictionary.
    """
    json_file = open_file(json_dict)
    return json.loads(json_file)


def yaml_parse(yaml_dict):
    """Convert from YAML to python

    Args:
        yaml_dict: Absolute or relative file address.

    Returns:
        dict: Returns the python dictionary.
    """
    yaml_file = open_file(yaml_dict)
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
