# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    ans=[0]*max((n+1),4)
    ans[1],ans[2],ans[3] = 1,2,4
    for z in range(4,n+1): ans[z]=ans[z-1]+ans[z-2]+ans[z-3]
    return ans[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()