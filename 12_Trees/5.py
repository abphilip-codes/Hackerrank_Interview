# https://www.hackerrank.com/challenges/balanced-forest/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf
from collections import Counter, defaultdict

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

def balancedForest(c, edges):
    def st(i,p):
        ans=0
        for z in a[i]:
            if z!=p: ans+=st(z,i)
        ans+=c[i]
        sc[ans],tl[i]=sc[ans]+1,ans
        return ans
    
    def me(i,p,path):
        s = tl[i]
        path.add(s)
        m = min((me(z,i,path) for z in a[i] if z!=p), default=inf)
        
        if (3*s<t):
            if (t+s)%2==0:
                if ((t+s)//2) in path: m = min(m,((t+s)//2)-2*s)
                if sc[((t-s)//2)]>0 and (((t-s)//2) not in path or sc[((t-s)//2)]>1): m = min(m,((t-s)//2)-s)
        elif (2*s in path or (t-s) in path or sc[s]>1): m = min(m,3*s-t)
        path.remove(s)
        return m
        
    n = len(c)
    a = [[] for z in range(n)]
    for z, y in edges:
        a[z-1].append(y-1)
        a[y-1].append(z-1)
    sc,tl = Counter(),{}
    t = st(0, None)
    m = me(0, None, set())
    return m if m < inf else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()