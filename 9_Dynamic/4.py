# https://www.hackerrank.com/challenges/decibinary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def decibinaryNumbers(x):
    d={}
    for z in range(0,100000):
        n,r=str(z)[::-1],0
        for y in range(len(n)): r+=int(n[y])*(2**y)
        d.update({z:r})
    ans=sorted(d.items(),key=lambda i:(i[1],i[0]))
    return(ans[x-1][0])        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()