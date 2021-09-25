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
    ans,n = 0,len(h)
    for z in range(n):
        a,b,c = z,z+1,0
        while(a>=0 and h[a]>=h[z]): a,c=a-1,c+1
        while(b<n and h[b]>=h[z]): b,c=b+1,c+1
        ans = max(ans,h[z]*c)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()