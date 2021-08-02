# https://www.hackerrank.com/challenges/new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    p,q,ans=list(range(len(q))),[i-1 for i in q],0
    for i in range(len(q)):
        if(q[i]-i)>2:
            print("Too chaotic")
            return
        for j in range(max(q[i]-1,0),i):
            if(q[j]>q[i]): ans+=1
    print(ans)
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)