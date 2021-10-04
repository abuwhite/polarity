# -*- coding: utf-8 -*-

"""polarity - Compares two configuration files and shows a difference.

Usage: polarity [options] <filepath1> <filepath2>

Options:
-h, --help           display help for command
-f, --format [type]  output format (default: "stylish")
-V, --version        output the version number

Examples:
    polarity -f plain file1.yml file2.json
        Property 'common.follow' was added with value: false
        Property 'common.setting2' was removed
        Property 'common.setting3' was updated. From true to [complex value]
        Property 'common.setting4' was added with value: 'blah blah'
        Property 'common.setting5' was added with value: [complex value]
        Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'
        Property 'common.setting6.ops' was added with value: 'vops'
        Property 'group1.baz' was updated. From 'bas' to 'bars'
        Property 'group1.nest' was updated. From [complex value] to 'str'
        Property 'group2' was removed
        Property 'group3' was added with value: [complex value]
        Property 'group4.default' was updated. From null to ''
        Property 'group4.foo' was updated. From 0 to null
        Property 'group4.isNested' was updated. From false to 'none'
        Property 'group4.key' was added with value: false
        Property 'group4.nest.bar' was updated. From '' to 0
        Property 'group4.nest.isNested' was removed
        Property 'group4.someKey' was added with value: true
        Property 'group4.type' was updated. From 'bas' to 'bar'

See also the documentation at https://github.com/znhv/polarity
"""

import argparse

from polarity.api.difference import generate_diff


class Args(object):
    """Args class."""

    def __init__(self, args=None):
        """Init class.

        Args:
            args: None
        """
        if args:
            self.parser = argparse.ArgumentParser(description="Test")
            self.parser.add_argument(
                "-t",
                "--test",
                default='test help'
            )
            self.parser.parse_args(args)
        else:
            self.parser = argparse.ArgumentParser(description="Polarity")
            self.parser.add_argument("first_file")
            self.parser.add_argument("second_file")
            self.parser.add_argument(
                "-f",
                "--format",
                help="output format (default: 'stylish')",
            )
            self.parser.parse_args(args)

    def get_args(self, args=None):
        """Get args.

        Args:
            args: None

        Returns:
            : Args
        """
        return self.parser.parse_args(args)


def run():
    """Скрипт запуска сравнения файлов."""
    args = Args()
    print(
        generate_diff(
            args.get_args().first_file,
            args.get_args().second_file,
            format_output=args.get_args().format,
        ),
    )


if __name__ == "__main__":
    run()
