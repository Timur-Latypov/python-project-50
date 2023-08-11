#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument("-f", "--format", help='set format of output')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.parse_args()


if __name__ == '__main__':
    main()