# https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    f = defaultdict(int)
    for z in s: f[z]+=1
    used_chars = defaultdict(int)
    remain_chars = dict(f)
    res = []
    
    def can_use(char):
        return (f[char] // 2 - used_chars[char]) > 0
    
    def can_pop(char):
        needed_chars = f[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            res.append(char)
        
        remain_chars[char] -= 1
    
    return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()