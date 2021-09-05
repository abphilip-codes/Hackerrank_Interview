# Standard Chartered Preliminary Test - I

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
    ans=stack=[]
    min1=99999999999
    max1=-9999999999
    for z in range(len(operations)):
        if(operations[z]=='push'):
            stack.append(x[z])
            if(min1>x[z]): min1=x[z]
            if(max1<x[z]): max1=x[z]
            temp = min1*max1
        else:
            stack.remove(x[z])
            min1=min(stack)
            max1=max(stack)
            temp = min1*max1
        x[z]=temp
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    result = maxMin(operations, x)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()