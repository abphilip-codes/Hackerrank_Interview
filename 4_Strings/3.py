# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    d={}
    for z in s:
        if z in d.keys(): d[z]+=1 
        else: d[z]=1
    check,count = d[next(iter(d))],0
    n,ones=[check],0
    for z in d:
        if(d[z]==1): ones+=1
        if(d[z]!=check): 
            count+=1
            n.append(d[z])
    if((count<=1 or count==len(d)-1) 
    and (abs(n[0]-n[-1])<=1 
    or (len(n)==2 and ones==1))): return "YES" 
    else: return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()