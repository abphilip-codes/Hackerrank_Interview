# https://www.hackerrank.com/challenges/minimum-time-required/problem 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()
    l = (goal//((len(machines)/machines[0])))
    u = (goal//((len(machines)/machines[-1])))+1
    while(l<u):
        n,t=(l+u)//2,0
        for z in machines: t+=(n//z)
        if(t>=goal): u=n
        else: l=n+1
    return int(l)


def getNumItems(machines, goal, num_days):
    total = 0
    for machine in machines:
        total += (num_days // machine)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()