# Standard Chartered Preliminary Test - II

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def maxDifference(px):
    ans,m=0,px[0]
    for z in range(1,len(px)):
        m=min(px[z],m)
        if(px[z]-m>ans): ans=px[z]-m
    if(ans==0): return -1
    else: return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    px_count = int(input().strip())

    px = []

    for _ in range(px_count):
        px_item = int(input().strip())
        px.append(px_item)

    result = maxDifference(px)

    fptr.write(str(result) + '\n')

    fptr.close()