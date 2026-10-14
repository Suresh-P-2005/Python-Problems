# Minimum Absolute Difference in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The absolute difference is the positive difference between two values $a$ and $b$, is written $|a-b|$ or $|b-a|$ and they are equal.  If $a = 3$ and $b = 2$, $|3-2| = |2-3| = 1$. Given an array of integers, find the minimum absolute difference between any two elements in the array.  

**Example**. 
$arr=[-2,2,4]$ 

There are $3$ pairs of numbers: $[-2,2], [-2,4]$ and $[2,4]$.  The absolute differences for these pairs are $|(-2) - 2| = 4$, $|(-2)-4| = 6$ and $|2 - 4| = 2$.  The minimum absolute difference is $2$.

**Function Description**  

Complete the *minimumAbsoluteDifference* function in the editor below.  It should return an integer that represents the minimum absolute difference between any pair of elements.  

minimumAbsoluteDifference has the following parameter(s):  

- *int arr[n]:* an array of integers  

**Returns**  

- *int:*  the minimum absolute difference found

**Input Format**

The first line contains a single integer $n$, the size of $arr$.		
The second line contains $n$ space-separated integers, $arr[i]$.   

**Constraints**

+ $2 \le n \le 10^5$  
+ $-10^9 \le arr[i] \le 10^9$  


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:24:15.389Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]

        if diff < min_diff:
            min_diff = diff

    return min_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem)