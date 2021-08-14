# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    l1,l2,ans=[0]*26,[0]*26,0
    for i in range(len(a)): l1[ord(a[i])-ord('a')]+=1
    for i in range(len(b)): l2[ord(b[i])-ord('a')]+=1
    for i in range(26): ans+=abs(l1[i]-l2[i])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()