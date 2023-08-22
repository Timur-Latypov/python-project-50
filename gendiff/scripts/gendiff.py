#!/usr/bin/env python3

import argparse
import gendiff.gendiff1 as gendiff1


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument("-f", "--format", help='set format of output',
                        default=gendiff1.stylish)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(gendiff1.generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
