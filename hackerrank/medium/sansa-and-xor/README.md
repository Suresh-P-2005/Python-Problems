# Sansa and XOR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Sansa has an array. She wants to find the value obtained by [XOR](http://en.wikipedia.org/wiki/XOR#Bitwise_operation)-ing the contiguous subarrays, followed by [XOR](http://en.wikipedia.org/wiki/XOR#Bitwise_operation)-ing the values thus obtained. Determine this value.  

**Example**   
$arr=[3,4,5]$   
```
Subarray	Operation	Result
3		None		3
4		None		4
5		None		5
3,4		3 XOR 4		7
4,5		4 XOR 5		1
3,4,5		3 XOR 4 XOR 5	2
```

Now we take the resultant values and XOR them together:

$3\oplus 4\oplus 5\oplus 7\oplus 1\oplus 2=6$.  Return $6$.   

**Function Description**  

Complete the *sansaXor* function in the editor below.  

sansaXor has the following parameter(s):  

- *int arr[n]:*  an array of integers  

**Returns**   

- *int:* the result of calculations  

**Input Format**

The first line contains an integer $t$, the number of the test cases.   

Each of the next $t$ pairs of lines is as follows:  
- The first line of each test case contains an integer $n$, the number of elements in $arr$.  
- The second line of each test case contains $n$ space-separated integers $arr[i]$.    


**Constraints**

$1 \le t \le 5$  
$2 \le n \le 10^5$  
$1 \le arr[i] \le 10^8 $  


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T13:04:06.392Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    n = len(arr)

    if n % 2 == 0:
        return 0

    result = 0

    for i in range(0, n, 2):
        result ^= arr[i]

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sansa-and-xor/problem)