# UBS Preliminary Test

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'ways' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER total
#  2. INTEGER k
#
def ways(total, k):
    ans,arr=0,[0]*(total+1)
    arr[0]=1
    for z in range(total):
        for y in range(1,k+1):
            if(y<=z+1): arr[z+1]+=arr[z+1-y]
    return arr[total]%1000000007
'''
def ways(total, k):
    a=[[0 for y in range(total+1)]for x in range(k+1)]
    for i in range(total+1):
        a[0][i]=0
        a[1][i]=1
    for z in range(k+1):
        a[z][0]=0
    for x in range(2,k+1):
        for y in range(1,total+1):
            if(x<y):
                a[x][y]=a[x-1][y]
            elif(x==y):
                a[x][y]=a[x-1][y]+1
            else: 
                a[x][y]=a[x-1][y]+a[x][y-x]
    return a[k-1][total-1]%100000007
'''
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    total = int(input().strip())

    k = int(input().strip())

    result = ways(total, k)

    fptr.write(str(result) + '\n')

    fptr.close()
