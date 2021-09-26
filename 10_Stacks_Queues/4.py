# https://www.hackerrank.com/challenges/min-max-riddle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    ans,n=[],len(arr)
    for z in range(1,n+1):
        temp=[]
        for y in range(n-z+1): temp.append(min(arr[y:y+z]))
        ans.append(max(temp))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()