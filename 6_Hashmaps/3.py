# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    ans,d = 0,{}
    for z in range(len(s)):
        for y in range(len(s)-z):
            t = ''.join(sorted(s[y:y+z+1]))
            d[t] = d.get(t,0)+1
    for k in d: ans+=(d[k]-1)*d[k]//2
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()