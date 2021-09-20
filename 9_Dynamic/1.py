# https://www.hackerrank.com/challenges/max-array-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    d = {} 
    d[0],d[1]=arr[0],max(arr[0], arr[1])
    for z,n in enumerate(arr[2:], start=2):
        d[z] = max(n,d[z-1],d[z-2]+n,d[z-2])
    return d[len(arr)-1]    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()