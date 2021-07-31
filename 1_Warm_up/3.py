# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    z=0
    res=0
    while(z<len(c)-2):
        if(c[z]==0 and c[z+2]==0):
            z+=2
            res+=1
        elif(c[z]==0 and c[z+1]==0):
            z+=1
            res+=1
        else: return res
    if(z<len(c)-1): return res+1  
    else: return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
