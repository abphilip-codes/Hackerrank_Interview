# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a,m):
    l,s=len(a),[[a[0]%m,0]]
    for z in range(1,l): s.append([(s[z-1][0]+(a[z]%m))%m,z])
    s,u=sorted(s),99999999999999
    for z in range(0,l-1): 
        if(s[z][1]>s[z+1][1]): u=min(s[z+1][0]-s[z][0],u)
    if(s[l-1][0]>m-u): u=m-s[l-1][0]
    return m-u

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()