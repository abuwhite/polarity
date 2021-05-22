#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
import json


def read_file(path):
    file = json.load(open(path))
    return file
