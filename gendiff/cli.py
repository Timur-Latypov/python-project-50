import argparse


def args_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output',
                        default='stylish', choices=['stylish', 'plain', 'json'])
    return parser.parse_args()
