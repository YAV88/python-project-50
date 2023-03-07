#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='First file to compare.')
    parser.add_argument('second_file', type=str, help='Second file to compare.')
    parser.add_argument('-f', '--format', help='Output format')


if __name__ == '__main__':
    main()
