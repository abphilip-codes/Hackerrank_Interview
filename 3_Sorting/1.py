# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    c=0
    for i in range(len(a)):
        for j in range(0,len(a)-1):
            if(a[j]>a[j+1]): a[j],a[j+1],c=a[j+1],a[j],c+1
    print("Array is sorted in {} swaps.".format(c))
    print("First Element:",a[0])
    print("Last Element:",a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)