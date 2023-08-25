#!/usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import make_json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    match args.format:
        case 'plain':
            formatter = plain
        case 'stylish':
            formatter = stylish
        case 'json':
            formatter = make_json
    print(generate_diff(args.first_file, args.second_file, formatter))


if __name__ == '__main__':
    main()
