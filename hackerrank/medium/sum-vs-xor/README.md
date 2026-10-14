# Sum vs XOR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer, find each such that:

-
-

where denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.

 **Example** 

There are four values that meet the criteria:

-
-
-
-

Return.

 **Function Description** 

Complete the sumXor function in the editor below.

sumXor has the following parameter(s):
-  *int n:*  an integer

 **Returns** 
-  *int:*  the number of values found

 **Input Format** 

A single integer,.

 **Constraints** 

-

 **Subtasks** 

- for of the maximum score.

 **Output Format** 

 **Sample Input 0** 

```
5

```

 **Sample Output 0** 

```
2

```

 **Explanation 0** 

For, the values and satisfy the conditions:

-
-

 **Sample Input 1** 

```
10

```

 **Sample Output 1** 

```
4

```

 **Explanation 1** 

For, the values,,, and satisfy the conditions:

-
-
-
-

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T09:40:39.827Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    if n == 0:
        return 1

    zero_bits = 0

    while n > 0:
        if n & 1 == 0:
            zero_bits += 1
        n >>= 1

    return 2 ** zero_bits
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sum-vs-xor/problem)