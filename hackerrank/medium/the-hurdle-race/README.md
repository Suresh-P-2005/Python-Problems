# The Hurdle Race

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A video player plays a game in which the character competes in a hurdle race.  Hurdles are of varying heights, and the characters have a maximum height they can jump.  There is a magic potion they can take that will increase their maximum jump height by $1$ unit for each dose.  How many doses of the potion must the character take to be able to jump all of the hurdles.  If the character can already clear all of the hurdles, return $0$.

**Example**  
$height = [1, 2, 3, 3, 2]$  
$k = 1$  

The character can jump $1$ unit high initially and must take $3 - 1 = 2$ doses of potion to be able to jump all of the hurdles.   

**Function Description**  

Complete the *hurdleRace* function in the editor below.    

hurdleRace has the following parameter(s):  

- *int k*: the height the character can jump naturally  
- *int height[n]*: the heights of each hurdle  

**Returns**  

- *int:* the minimum number of doses required, always $0$ or more

**Input Format**

The first line contains two space-separated integers $n$ and $k$, the number of hurdles and the maximum height the character can jump naturally.  	
The second line contains $n$ space-separated integers $height[i]$ where $0 \le i \lt n$.

**Constraints**

* $1 \le n, k \le 100$  
* $1 \le height[i] \le 100$  

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:20:25.711Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    tallest = max(height)

    if tallest > k:
        return tallest - k
    else:
        return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/the-hurdle-race/problem)