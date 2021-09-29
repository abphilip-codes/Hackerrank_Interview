# https://www.hackerrank.com/challenges/torque-and-development/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def dfs(s,a,b):
    b[s]=True
    cost=0
    for i in a[s]:
        if(not b[i]): cost+=(dfs(i,a,b)+1)
    return cost

def roadsAndLibraries(n, c_lib, c_road, cities):
    if(c_lib<c_road or cities==[]): return c_lib*n
    a,b,c=[[0] for z in range(n+1)],[False]*(n+1),0
    for z in range(1,n+1): a[z][0]=z
    for z in range(m):
        a[cities[z][0]].append(cities[z][1])
        a[cities[z][1]].append(cities[z][0])
    for z in range(1,n+1):
        if(not b[z]): c+=dfs(z,a,b)
    ans=(((c)*c_road)+((n-c)*c_lib))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()