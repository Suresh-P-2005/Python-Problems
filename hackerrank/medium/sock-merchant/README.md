# Sales by Match

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

**Example**   
$n = 7$   
$ar = [1, 2, 1, 2, 1, 3, 2]$   

There is one pair of color $1$ and one of color $2$.  There are three odd socks left, one of each color.  The number of pairs is $2$.  

**Function Description**  

Complete the *sockMerchant* function in the editor below.     

sockMerchant has the following parameter(s):  

- *int n:* the number of socks in the pile   
- *int ar[n]:* the colors of each sock   

**Returns**   

- *int:* the number of pairs   

**Input Format**

The first line contains an integer $n$, the number of socks represented in $ar$. 		
The second line contains $n$ space-separated integers, $ar[i]$, the colors of the socks in the pile.

**Constraints**

* $1 \le n \le 100$
* $1 \le ar[i] \le 100$ where $0 \le i < n$


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T12:22:30.009Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    color_counts = {}
    
    # Step 1: Count how many times each sock color appears
    for sock in ar:
        color_counts[sock] = color_counts.get(sock, 0) + 1
        
    # Step 2: Calculate pairs using integer division (// 2)
    total_pairs = 0
    for count in color_counts.values():
        total_pairs += count // 2
        
    return total_pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sock-merchant/problem)