# Sherlock and Squares

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Watson likes to challenge Sherlock's math ability.  He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints.  Sherlock must determine the number of *square integers* within that range.

**Note**: A square integer is an integer which is the square of an integer, e.g. $1, 4, 9, 16, 25$. 

**Example**  
$a = 24$  
$b = 49$  

There are three square integers in the range: $25, 36$ and $49$.  Return $3$.   

**Function Description**

Complete the *squares* function in the editor below.  It should return an integer representing the number of square integers in the inclusive range from $a$ to $b$.  

squares has the following parameter(s):  

- *int a:* the lower range boundary
- *int b:* the upper range boundary  

**Returns**  

- *int:* the number of square integers in the range

**Input Format**

The first line contains $q$, the number of test cases.   
Each of the next $q$ lines contains two space-separated integers, $a$ and $b$, the starting and ending integers in the ranges.     


**Constraints**

$1 \le q \le 100$  
$1 \le a \le b \le 10^9$  


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:47:12.512Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    return int(b ** 0.5) - int((a - 1) ** 0.5)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sherlock-and-squares/problem)