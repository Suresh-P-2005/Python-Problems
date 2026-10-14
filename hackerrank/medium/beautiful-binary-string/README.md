# Beautiful Binary String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring.

In one step, Alice can change a to a or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

 **Example** 

She can change any one element and have a beautiful string.

 **Function Description** 

Complete the  *beautifulBinaryString*  function in the editor below.

beautifulBinaryString has the following parameter(s):

- string b: a string of binary digits

 **Returns** 

- int: the minimum moves required

 **Input Format** 

The first line contains an integer, the length of binary string.
The second line contains a single binary string.

 **Constraints** 

-
-.

 **Output Format** 

Print the minimum number of steps needed to make the string beautiful.

 **Sample Input 0** 

```
STDIN       Function
-----       --------
7           length of string n = 7
0101010     b = '0101010'

```

 **Sample Output 0** 

```
2  

```

 **Explanation 0:** 

In this sample,

The figure below shows a way to get rid of each instance of :

Make the string beautiful by changing characters (and).

 **Sample Input 1** 

```
5
01100

```

 **Sample Output 1** 

```
0

```

 **Sample Case 1:** 

In this sample

 **Explanation 1** 

The substring does not occur in, so the string is already beautiful in moves.

 **Sample Input 2** 

```
10
0100101010

```

 **Sample Output 2** 

```
3

```

 **Explanation 2** 

In this sample

One solution is to change the values of to form a beautiful string.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:59:30.491Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    count = 0
    i = 0

    while i < len(b) - 2:
        if b[i:i + 3] == "010":
            count += 1
            i += 3
        else:
            i += 1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/beautiful-binary-string/problem)