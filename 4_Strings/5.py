# https://www.hackerrank.com/challenges/common-child/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    s = [0]*len(s1)
    for c in s2:
        m = 0
        for z in range(len(s1)):
            t = s[z]
            if(c==s1[z]): s[z] = m+1
            if(s[z]>0 and t>0): m = max(t,m)
    return max(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()