# https://www.hackerrank.com/challenges/special-palindrome-again/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    l,c,r,ans = [],0,None,0
    for z in range(n):
        if(s[z] == r): c+=1
        else:
            if(r is not None): l.append((r, c))
            r,c = s[z],1
    l.append((r, c))

    for z in l: ans+=(z[1]*(z[1]+1))//2
    for z in range(1, len(l) - 1):
        if(l[z-1][0]==l[z+1][0] and l[z][1]==1): ans+=min(l[z-1][1],l[z+1][1])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
