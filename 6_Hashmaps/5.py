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
    freqs = defaultdict(set)
    for command, value in queries:
        freq = d.get(value, 0)
        if command == 1:
            d[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            d[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            ans.append(1 if freqs[value] else 0)
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