#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    result = []

    for num in range(p, q + 1):
        square = num * num
        digits = len(str(num))

        left = str(square)[:-digits]
        right = str(square)[-digits:]

        left_num = int(left) if left else 0
        right_num = int(right)

        if left_num + right_num == num:
            result.append(num)

    if result:
        print(*result)
    else:
        print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
