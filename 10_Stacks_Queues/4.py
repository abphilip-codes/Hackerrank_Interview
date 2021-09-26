# https://www.hackerrank.com/challenges/min-max-riddle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    l = []
    d = {}
    a = arr[:]+[-float('inf')]
    for z in range(len(a)):
        k = z
        while(l and a[z]<=l[-1][0]):
            n,k = l.pop()
            d[z-k] = max(d.get(z-k,0),n)
        l.append((a[z],k))
    ans, m = [0]*len(arr), 0
    for z in reversed(range(len(arr))):
        m = max(d.get(z+1,m),m)
        ans[z] = m
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()