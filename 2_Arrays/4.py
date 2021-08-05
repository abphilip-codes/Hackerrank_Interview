# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(A):
    k=0
    for i in range(len(A)):
        m = A.index(min(A[i:])) 
        if(m!=i):
            A[i], A[m] = A[m], A[i]
            k+=1
    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()