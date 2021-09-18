# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self,d): self.data=d
    
def tree(indexes):
    f = lambda x: None if (x==-1) else Node(x)
    c = [list(map(f,x)) for x in indexes]
    nodes = {n.data: n for n in filter(None, sum(c,[]))}
    nodes[1] = Node(1)
    for z,p in enumerate(c):
        nodes[z+1].left = p[0]
        nodes[z+1].right = p[1]
    return nodes[1]

def inorder(root):
    a = []
    while a or root:
        if root:
            a.append(root)
            root = root.left
        else:
            root = a.pop()
            yield root.data
            root = root.right
        
def swapNodes(indexes, queries):
    root=tree(indexes)
    for z in queries:
        h=1
        q=deque([root])
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if (h%z==0): n.left,n.right=n.right,n.left
                q+=filter(None,(n.left, n.right))
            h+=1
        yield inorder(root)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()