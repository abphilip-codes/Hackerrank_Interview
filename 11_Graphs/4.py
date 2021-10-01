# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    def c(z,y):
        if (0<=z<len(grid) and 0<=y<len(grid[z]) and grid[z][y]==1):
            grid[z][y] = 0
            return 1+sum(c(x,w) for x in range(z-1,z+2) for w in range(y-1,y+2))
        return 0
    return max(c(z,y) for z in range(len(grid)) for y in range(len(grid[z])))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()