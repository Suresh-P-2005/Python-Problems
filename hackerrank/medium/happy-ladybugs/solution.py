#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
def happyLadybugs(b):
    from collections import Counter

    count = Counter(b)

    if '_' not in b:
        for i in range(len(b)):
            if (i == 0 or b[i] != b[i - 1]) and \
               (i == len(b) - 1 or b[i] != b[i + 1]):
                return "NO"
        return "YES"

    for color in count:
        if color != '_' and count[color] < 2:
            return "NO"

    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
