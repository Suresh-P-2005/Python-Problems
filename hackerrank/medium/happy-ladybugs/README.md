# Happy Ladybugs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Happy Ladybugs is a board game having the following properties:

* The board is represented by a string, $b$, of length $n$. The $i^{th}$ character of the string, $b[i]$, denotes the $i^{th}$ cell of the board.
    * If $b[i]$ is an underscore (i.e., `_`), it means the $i^{th}$ cell of the board is empty.
    * If $b[i]$ is an uppercase English alphabetic letter (ascii[A-Z]), it means the $i^{th}$ cell contains a ladybug of color $b[i]$.
    * String $b$ will not contain any other characters.
- A ladybug is *happy* only when its left or right adjacent cell (i.e., $b[i \pm 1]$) is occupied by another ladybug having the same color.
- In a single move, you can move a ladybug from its current position to any empty cell. 
<br>

Given the values of $n$ and $b$ for $g$ games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, return `YES` if all the ladybugs can be made happy through some number of moves.  Otherwise, return `NO`.      
**Example**     
$b=[YYR\_B\_BR]$    

You can move the rightmost $B$ and $R$ to make $b=[YYRRBB\_\_]$ and all the ladybugs are happy. Return `YES`.   

**Function Description**  

Complete the *happyLadybugs* function in the editor below.   

happyLadybugs has the following parameters:

- *string b:* the initial positions and colors of the ladybugs   

**Returns**   

- *string:* either `YES` or `NO`   

**Input Format**

The first line contains an integer $g$, the number of games.  

The next $g$ pairs of lines are in the following format:  

- The first line contains an integer $n$, the number of cells on the board.  
- The second line contains a string $b$ that describes the $n$ cells of the board.  

**Constraints**

* $1 \le g,n \le 100$  
* $b[i] \in \{\_,ascii[A-Z]\}$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T10:22:22.390Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
def happyLadybugs(b):
    from collections import Counter

    count = Counter(b)

    if '_' not in b:
        for i in range(len(b)):
            if (i == 0 or b[i] != b[i - 1]) and \
               (i == len(b) - 1 or b[i] != b[i + 1]):
                return "NO"
        return "YES"

    for color in count:
        if color != '_' and count[color] < 2:
            return "NO"

    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/happy-ladybugs/problem)