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
    s=c=[0]*n
    for i in range(len(arr)):
            if i == 0 or s[i-1] == 1:
                    s[i] = get_num_descending(arr, i)
            else:
                    s[i] = s[i-1] - 1
            c[i] = s[i] if arr[i] <= arr[i-1] else max(s[i], c[i-1]+1)
    return sum(c)

def get_num_descending(arr, i):
    ret = 1
    while i + 1 < len(arr):
            if arr[i] > arr[i+1]:
                    ret += 1
                    i += 1
            else:
                    return ret
    return ret

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