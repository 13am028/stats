#!/usr/bin/env python
import sys
import numpy as np


def print_util(temp):
    print('mean:', np.mean(temp))
    print('std:', np.std(temp))
    print('min:', min(temp))
    print('max:', max(temp))
    print('n:', len(temp))


if __name__ == "__main__":
    nums = []
    for i in range(1, len(sys.argv)):
        temp = []
        path = sys.argv[i]
        try:
            f = open(path, 'r')
            for line in f:
                num = line.strip()  # or some other preprocessing
                nums.append(int(num))
                temp.append(int(num))

            print(path)
            print_util(temp)
            f.close()
        except Exception as e:
            print(f"Unable to open {path}: {e}", file=sys.stderr)

    print('combined:')
    print_util(nums)
