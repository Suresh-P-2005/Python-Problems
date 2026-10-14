# Missing Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two arrays of integers, find which elements in the second array are missing from the first array.

**Example**  
$arr = [7, 2, 5, 3, 5, 3]$  
$brr = [7, 2, 5, 4, 6, 3, 5, 3]$

The $brr$ array is the orginal list.  The numbers missing are $[4, 6]$.  

**Notes**  

* If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number. 
* Return the missing numbers sorted ascending. 
* Only include a missing number once, even if it is missing multiple times. 
* The difference between the maximum and minimum numbers in the original list is less than or equal to $100$.  

**Function Description**  

Complete the *missingNumbers* function in the editor below.  It should return a sorted array of missing numbers.  

missingNumbers has the following parameter(s):

- *int arr[n]:* the array with missing numbers   
- *int brr[m]:* the original array of numbers   

**Returns**   

- *int[]:* an array of integers   

**Input Format**

There will be four lines of input:  

 $n$ - the size of the first list, $arr$  
 The next line contains $n$ space-separated integers $arr[i]$  
 $m$ - the size of the second list, $brr$  
 The next line contains $m$ space-separated integers $brr[i]$  


**Constraints**

* $1 \le n, m \le 2 \times 10^{5}$  
* $ n \le m $
* $1 \le brr[i] \le 10^{4}$  
* $max(brr) - min(brr) \le 100$


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T10:41:49.048Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    from collections import Counter

    count_arr = Counter(arr)
    count_brr = Counter(brr)

    result = []

    for num in count_brr:
        if count_brr[num] > count_arr[num]:
            result.append(num)

    return sorted(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/missing-numbers/problem)