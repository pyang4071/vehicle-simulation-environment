#!/usr/bin/env python3

import argparse
import pathlib

from simulation import test_module


def main():
    parser = argparse.ArgumentParser(
        description="Simulates the movement of a vehicle \
        in a 2D virtual enviroment with obstacles"
    )
    parser.add_argument(
        "-i", "--input", default=pathlib.Path("input.yml"), type=pathlib.Path
    )
    parser.add_argument(
        "-o", "--output", default=pathlib.Path("output.yml"), type=pathlib.Path
    )
    args = parser.parse_args()
    print(args)
    test_module.testing()


if __name__ == "__main__":
    main()
