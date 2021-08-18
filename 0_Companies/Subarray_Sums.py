#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries, zeroes):
    ans=[]
    for q in queries:
        s=numbers[q[1]]-numbers[q[0]-1]
        s+=q[2]*(zeroes[q[1]]-zeroes[q[0]-1])
        ans.append(s)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = [0]
    zeroes = [0]
    numbers_item = 0
    zero = 0
    for i in range(numbers_count):
        numbers_item += int(input().strip())
        numbers.append(numbers_item)
        if(numbers[i+1]==numbers[i]): 
            zero+=1
            zeroes.append(zero)
        else: zeroes.append(zero)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries, zeroes)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()