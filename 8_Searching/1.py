# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    s={}
    for z,k in enumerate(cost):
        if ((money-k) in s): print(s[money-k],z+1)
        s[k]=z+1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)