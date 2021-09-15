# https://www.hackerrank.com/challenges/triple-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a,b,c = list(sorted(set(a))),list(sorted(set(b))),list(sorted(set(c)))
    x=y=z=ans=0    
    while(y<len(b)):
        while(x<len(a) and a[x]<=b[y]): x+=1
        while(z<len(c) and c[z]<=b[y]): z+=1
        ans,y=ans+x*z,y+1    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()