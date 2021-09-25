# https://www.hackerrank.com/challenges/largest-rectangle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    ans = 0
    for z in range(len(h)):
        c = 0
        for a in range(z,-1,-1):
            if(h[a]<h[z]): break 
            c+=1
        for b in range(z+1,len(h)):
            if(h[b]<h[z]): break 
            c+=1
        ans = max(ans,h[z]*c)
        print("C:",c)
        print("B:",b)
        print("A:",a)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()