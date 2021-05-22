#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gendiff import cli, generate_diff


def main():
    args = cli.run()
    generate_diff.output(args)


if __name__ == "__main__":
    main()
