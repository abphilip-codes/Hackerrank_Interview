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
    visited_nodes = set()
    q = deque()
    q.appendleft((startX, startY, 0))
    neighboring_nodes = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    grid_dimension = len(grid)
    while q:
        (current_x, current_y, dist) = q.pop()
        new_dist = dist + 1
        for neighboring_node_diff in neighboring_nodes:
            x = current_x + neighboring_node_diff[0]
            y = current_y + neighboring_node_diff[1]
            while (0 <= x < grid_dimension) and (0 <= y < grid_dimension) and (grid[x][y] != 'X'):
                if (x, y) == (goalX, goalY):
                    return new_dist
                elif (x, y) not in visited_nodes:
                    q.appendleft((x, y, new_dist))
                    visited_nodes.add((x, y))
                x += neighboring_node_diff[0]
                y += neighboring_node_diff[1]

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