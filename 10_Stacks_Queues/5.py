# https://www.hackerrank.com/challenges/castle-on-the-grid/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    v = set()
    q = deque()
    q.appendleft((startX, startY, 0))
    n = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    while q:
        (cx, cy, dist) = q.pop()
        for d in n:
            x=cx+d[0]
            y=cy+d[1]
            while (0<=x<len(grid)) and (0<=y<len(grid)) and (grid[x][y]!='X'):
                if (x, y) == (goalX, goalY): return dist+1
                elif (x, y) not in v:
                    q.appendleft((x, y, dist+1))
                    v.add((x, y))
                x+=d[0]
                y+=d[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()