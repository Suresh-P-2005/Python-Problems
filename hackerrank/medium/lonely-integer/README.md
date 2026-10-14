# Lonely Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers, where all elements but one occur twice, find the unique element.  

**Example**  
$a = [1, 2, 3, 4, 3, 2, 1]$  

The unique element is $4$.  

**Function Description**  

Complete the *lonelyinteger* function in the editor below.   

lonelyinteger has the following parameter(s):  

- *int a[n]*: an array of integers   

**Returns**  

- *int:* the element that occurs only once  

**Input Format**

The first line contains a single integer, $n$, the number of integers in the array.		
The second line contains $n$ space-separated integers that describe the values in $a$.

**Constraints**

- $1 \le n \lt 100$  
- It is guaranteed that $n$ is an odd number and that there is one unique element.  
- $0 \le a[i] \le 100$, where $0 \le i \lt n$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T09:31:21.384Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    result = 0

    for num in a:
        result ^= num

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/lonely-integer/problem)