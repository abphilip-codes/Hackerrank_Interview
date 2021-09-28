# https://www.hackerrank.com/challenges/poisonous-plants/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    a,ans = [],-99999999
    for z in p:
        y=1
        while(a and a[-1][0]>=z):
            _,d = a.pop()
            y = max(y,d+1)
        if not a: y = 0
        ans = max(ans,y)
        a.append((z,y))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()