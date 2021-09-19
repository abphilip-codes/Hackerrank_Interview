# https://www.hackerrank.com/challenges/making-candies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m,w,p,n):
    c=i=0
    s=sys.maxsize
    while(c<n):
        ans=(p-c)//(m*w)
        if(ans<=0):
            k=(c//p)+m+w
            if (m>w):
                m=max(m,math.ceil(k/2))
                w=k-m
            else:
                w=max(w,math.ceil(k/2))
                m=k-w
            c%=p
            ans=1
        c+=ans*m*w
        i+=ans
        s=min(s,i+math.ceil((n-c)/(m*w)))
    return min(i,s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()