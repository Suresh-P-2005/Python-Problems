# Palindrome Index

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a [palindrome](https://en.wikipedia.org/wiki/Palindrome).  There may be more than one solution, but any will do.  If the word is already a palindrome or there is no solution, return _-1_.  Otherwise, return the index of a character to remove.  

**Example**  
$s = \text{"bcbc"}$  

Either remove *'b'* at index $0$ or *'c'* at index $3$.  

**Function Description**  

Complete the *palindromeIndex* function in the editor below.    

palindromeIndex has the following parameter(s):  

- *string s:* a string to analyze  

**Returns**  

- *int:* the index of the character to remove or $-1$  

**Input Format**

The first line contains an integer $q$, the number of queries.		
Each of the next $q$ lines contains a query string $s$.

**Constraints**

- $1 \le q \le 20$  
- $1 \le \text{length of } s \le 10^5 + 5$  
- All characters are in the range ascii[a-z].

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T09:43:10.522Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try removing the left character
            if s[left + 1:right + 1] == s[left + 1:right + 1][::-1]:
                return left

            # Otherwise, remove the right character
            return right

        left += 1
        right -= 1

    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/palindrome-index/problem)