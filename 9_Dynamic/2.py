# https://www.hackerrank.com/challenges/abbr/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    m,n = len(a),len(b)
    d = [[False]*(m+1) for _ in range(n+1)]
    d[0][0] = True
    for z in range(n+1):
        for y in range(m+1):
            if (z==0 and y!=0):
                d[z][y] = a[y-1].islower() and d[z][y-1]
            elif (z!=0 and y!=0):
                if (a[y-1] == b[z-1]): d[z][y] = d[z-1][y-1]
                elif (a[y-1].upper() == b[z-1]): d[z][y] = d[z-1][y-1] or d[z][y-1]
                elif not (a[y-1].isupper() and b[z-1].isupper()): d[z][y] = d[z][y-1]
    return "YES" if (d[n][m]) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()