# https://www.hackerrank.com/challenges/maximum-xor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    ans,t,k = [],{},len(bin(max(arr+queries)))-2 
    for z in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = t
        for c in z: node = node.setdefault(c, {})
    for z in queries:
        node,s = t,''
        for c in '{:b}'.format(z).zfill(k) :
            a = str(int(c)^1) if str(int(c)^1) in node else c 
            node,s = node[a],s+a
        ans.append(int(s,2)^z) 
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()