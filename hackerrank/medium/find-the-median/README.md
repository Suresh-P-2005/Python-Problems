# Find the Median

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The median of a list of numbers is essentially its middle element after sorting.  The same number of elements occur after it as before.  Given a list of numbers with an odd number of elements, find the [median](https://en.wikipedia.org/wiki/Median)?

**Example**   
$arr = [5, 3, 1, 2, 4]$   

The sorted array $arr' = [1, 2, 3, 4, 5]$.  The middle element and the median is $3$.  

**Function Description**

Complete the *findMedian* function in the editor below.  

findMedian has the following parameter(s):  

- *int arr[n]:* an unsorted array of integers  

**Returns**  

- *int:* the median of the array

**Input Format**

The first line contains the integer $n$, the size of $arr$.  
The second line contains $n$ space-separated integers $arr[i]$



**Constraints**

- $1 \le n \le 1000001$   
- $n$ is odd
- $-10000 \le arr[i] \le 10000$   



**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T10:38:26.302Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/find-the-median/problem)