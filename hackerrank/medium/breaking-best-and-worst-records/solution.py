#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_score = scores[0]
    lowest_score = scores[0]
    highest_breaks = 0
    lowest_breaks = 0
    for score in scores:
        if score > highest_score:
            highest_score = score
            highest_breaks += 1
        elif score < lowest_score:
            lowest_score = score
            lowest_breaks += 1
    return [highest_breaks, lowest_breaks]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
