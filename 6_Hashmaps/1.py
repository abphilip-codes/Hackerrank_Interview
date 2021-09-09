# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    d,k = {},0
    for word in magazine:
        if(word in d): d[word]+=1
        else: d[word]=1
    for word in note:
        if(word not in d or d[word]<1): k=1
        else: d[word]-=1
    print("No") if(k==1) else print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)