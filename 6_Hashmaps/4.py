# https://www.hackerrank.com/challenges/count-triplets-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    c,d,pairs=0,{},{}
    for z in reversed(arr):
        if (z*r) in pairs: c+=pairs[z*r]
        if (z*r) in d: pairs[z] = pairs.get(z,0)+d[z*r]
        d[z] = d.get(z,0)+1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()