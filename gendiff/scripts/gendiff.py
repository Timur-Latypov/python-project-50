#!/usr/bin/env python3

import argparse
import gendiff.gendiff as gendiff
from gendiff.formaters.stylish_format import stylish
from gendiff.formaters.plain_format import plain


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
            formater = plain
        case 'stylish':
            formater = stylish
    print(gendiff.generate_diff(
        args.first_file, args.second_file, formater))


if __name__ == '__main__':
    main()
