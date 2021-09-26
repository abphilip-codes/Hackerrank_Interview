# https://www.hackerrank.com/challenges/min-max-riddle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # ans,n=[],len(arr)
    # for z in range(1,n+1):
    #     temp=[]
    #     for y in range(n-z+1): temp.append(min(arr[y:y+z]))
    #     ans.append(max(temp))
    # return ans

    stack = []
    d = {}
    # to pop all the remaining elements in the stack
    tmp = arr[:] + [-float('inf')]
    # we get how big is the window for which this item is min
    for i in range(len(tmp)):
        indexed = i
        while stack and tmp[i] <= stack[-1][0]:
            n, indexed = stack.pop()
            d[i - indexed] = max(d.get(i - indexed,0), n)
        stack.append((tmp[i], indexed))
    # we get the max's per window size
    res, current = [0]*len(arr), 0
    for i in reversed(range(len(arr))):
        current = max(d.get(i+1, current), current)
        res[i] = current
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()