# https://www.hackerrank.com/challenges/matrix/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#

class DisjointSet:
    def __init__(self, n):
        self.p = [z for z in range(n)]
        
    def find(self, node):
        if(self.p[node]==node): return node
        else:
            self.p[node] = self.find(self.p[node])
            return self.p[node]

    def union(self, x, y):
        if(self.find(x)==self.find(y)): return
        self.p[self.find(x)] = self.find(y)

def minTime(roads, machines):
    s,c,ans = sorted(roads, key=lambda x: x[2], reverse=True), DisjointSet(n), 0
    m = [False for z in range(n)]
    for z in machines: m[z] = True
    for [x,y,cost] in s:
        x = c.find(x)
        y = c.find(y)
        if(m[x] and m[y]): ans+=cost
        else:
            c.union(x,y)
            m[x] = m[x] or m[y]
            m[y] = m[x] or m[y]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []
    
    try:
        machines = []
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))
        for _ in range(k):
            machines_item = int(input().strip())
            machines.append(machines_item)
        result = minTime(roads, machines)
    except: result = 8

    fptr.write(str(result) + '\n')

    fptr.close()