# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    global count
    if(len(arr)>1):
        n = len(arr)
        m = n//2
        a,b = arr[:m],arr[m:n]

        countInversions(a)
        countInversions(b)
        
        x=y=z=0
        n1,n2=m,n-m
        while(x<n1 and y<n2):
            if(a[x]<=b[y]): arr[z],x,z = a[x],x+1,z+1
            else: arr[z],y,z,count = b[y],y+1,z+1,count+n1-x
        while(x<n1): arr[z],x,z = a[x],x+1,z+1
        while(y<n2): arr[z],y,z = b[y],y+1,z+1
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))
        
        count = 0

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()