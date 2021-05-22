#!/usr/bin/python3

import os
import json


def get_file(path):
    file = json.load(open(path))
    print(file)
