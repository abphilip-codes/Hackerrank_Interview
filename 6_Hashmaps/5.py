# https://www.hackerrank.com/challenges/frequency-queries/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    ans,d = [],{}
    freq = defaultdict(set)
    for (i,v) in queries:
        f = d.get(v,0)
        if(i==1):
            d[v]=f+1
            freq[f].discard(v)
            freq[f+1].add(v)
        elif(i==2):
            d[v] = max(0,f-1)
            freq[f].discard(v)
            freq[f-1].add(v)
        elif(i==3):
            ans.append(1 if freq[v] else 0)
    return ans  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()