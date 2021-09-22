# https://www.hackerrank.com/challenges/candies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n,arr):
    s,c = [0]*n,[0]*n
    for z in range(n):
        if (z==0 or s[z-1]==1):
            s[z]+=1
            for y in range(z,n-1):
                if (arr[y]>arr[y+1]): s[z]+=1
                else: break
        else: s[z] = s[z-1]-1
        c[z] = s[z] if (arr[z]<=arr[z-1]) else max(s[z],c[z-1]+1)
    return sum(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()