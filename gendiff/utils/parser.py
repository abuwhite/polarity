# -*- coding: utf-8 -*-

"""Parser."""

import json


def read_file(path):
    """Открываем и возвращаем данные из файла.

    Args:
        path: Абсолютный или относительный адрес файла.

    Returns:
        set: Возвращаем данные из файла.
    """
    with open(path) as file_obj:
        return json.load(file_obj)
