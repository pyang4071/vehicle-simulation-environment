#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(prog = 'main.py',
                                     description = 'parsing input/output')
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()


