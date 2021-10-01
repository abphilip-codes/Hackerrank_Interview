# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue
from collections import deque

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = {z+1: [] for z in range(graph_nodes)}
    for z in range(len(graph_from)):
        g[graph_from[z]].append(graph_to[z])
        g[graph_to[z]].append(graph_from[z])
    t = []
    for i in range(len(ids)):
        if (ids[i]==val): t.append(i+1)
    ans=-1
    for node in t:
        #w = check(g,t,node,ans)
        v = set()
        q = Queue()
        q.put((node, 0))
        while (q.empty()!=True):
            n,w = q.get()
            if (n in v): continue
            if (n in t and n!=node): break
            v.add(n)
            if (w==ans): w=-1
            for z in g[n]:
                if z not in v: q.put((z,w+1))
        else: w=-1
        if (w>0 and w<ans or ans==-1): ans=w
    return ans

def check(g,t,node,ans=-1):
    v = set()
    q = Queue()
    q.put((node, 0))
    while (q.empty()!=True):
        n,w = q.get()
        if (n in v): continue
        if (n in t and n!=node): return w
        v.add(n)
        if (w==ans): return -1
        for z in g[n]:
            if z not in v: q.put((z,w+1))
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()