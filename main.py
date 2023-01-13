#!/usr/bin/env python

if __name__ == "__main__":
    import sys
    import numpy as np

    nums = []
    with open(sys.argv[1]) as file:
        for line in file:
            num = line.strip()  # or some other preprocessing
            nums.append(int(num))

    print(np.mean(nums))
    print(np.std(nums))
    print(min(nums))
    print(max(nums))
