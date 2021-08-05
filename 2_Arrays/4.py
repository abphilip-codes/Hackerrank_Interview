# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    k,z=0,dict(zip(a,range(1,len(a)+1)))
    for i in range(1,len(a)+1):
        if z[i]!=i: 
            z[a[i-1]]=z[i]
            a[z[i]-1]=a[i-1]
            k+=1
    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()