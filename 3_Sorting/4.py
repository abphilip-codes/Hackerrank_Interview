# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(e, d):
    f,ans = {},0
    def call(a):
        t = 0
        for i in range(201): 
            if (i in f): t = t + f[i]
            if (t >= a): return i
    for i in range(len(e)-1):
        if (e[i] in f): f[e[i]]+=1
        else: f[e[i]]=1
        if (i+1>=d):
            if (d%2==0): m = (call(d//2)+call(d//2+1))/2
            else: m = call(d/2)
            if e[i+1]>= (m*2) :
                ans+=1
                print("notify: ",ans)
            f[expenditure[i-d+1]]-=1
    return ans    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()