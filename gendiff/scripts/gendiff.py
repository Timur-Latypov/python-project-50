#!/usr/bin/env python3

from gendiff.cli import args_parser
from gendiff.gendiff import generate_diff


def main():
    args = args_parser()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
