# https://www.hackerrank.com/challenges/friend-circle-queries/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    k,g,ans,m  = {},{},[0],0
    for z,y in queries:
        if (z not in k): g[z],k[z] = set([z]),z
        if (y not in k): g[y],k[y] = set([y]),y
        if (k[z]!=k[y]):
            z,y=k[z],k[y]
            if (len(g[y])>len(g[z])): z,y=y,z
            g[z]|=g[y]
            for x in g[y]: k[x]=z
            del g[y]
        ans.append(max(ans[-1], len(g[k[z]])))
    return ans[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()