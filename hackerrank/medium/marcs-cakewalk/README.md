# Marc's Cakewalk

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories.  If Marc has eaten $j$ cupcakes so far, after eating a cupcake with $c$ calories he must walk *at least* $2^j \times c$  miles to maintain his weight.

**Example**    
$calorie = [5, 10, 7]$   

If he eats the cupcakes in the order shown, the miles he will need to walk are $(2^0\times 5) + (2^1\times 10) + (2^2\times 7) = 5 + 20 + 28 = 53$.  This is not the minimum, though, so we need to test other orders of consumption.  In this case, our minimum miles is calculated as $(2^0\times 10) + (2^1\times 7) + (2^2 \times 5) = 10 + 14 + 20 = 44$.

Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes *in any order*.  

**Function Description**  

Complete the *marcsCakewalk* function in the editor below.  

marcsCakewalk has the following parameter(s):  

- *int calorie[n]:* the calorie counts for each cupcake   

**Returns**   

- *long:* the minimum miles necessary

**Input Format**

The first line contains an integer $n$, the number of cupcakes in $calorie$.  
The second line contains $n$ space-separated integers, $calorie[i]$.


**Constraints**

- $1 \le n \le 40$
- $1 \le c[i] \le 1000$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:34:34.514Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0

    for i in range(len(calorie)):
        miles += calorie[i] * (2 ** i)

    return miles
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/marcs-cakewalk/problem)