# https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    l=[]
    try:
        for z in s:
            if(z==']' and l[-1]=='['): l.pop(-1)
            elif(z==')' and l[-1]=='('): l.pop(-1)
            elif(z=='}' and l[-1]=='{'): l.pop(-1)
            else: l.append(z)
    except: return "NO"
    return "YES" if(l==[]) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()