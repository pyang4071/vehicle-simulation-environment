#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Simulates the movement of a vehicle in a 2D virtual enviroment with obstacles')
    parser.add_argument('-i', '--input', default=argparse.SUPPRESS, type = argparse.FileType('r', encoding = "utf-8"))
    parser.add_argument('-o', '--output', default=argparse.SUPPRESS, type = argparse.FileType('w', encoding = "utf-8"))
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
