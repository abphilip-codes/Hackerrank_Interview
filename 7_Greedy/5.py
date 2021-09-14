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
    r,ans,u = dict(f),[],defaultdict(int)
    
    for z in reversed(s):
        if ((f[z]//2-u[z])>0):
            while(ans and ans[-1]>z and u[z]+r[z]-1>=f[z]//2): u[ans.pop()]-=1
            u[z]+=1
            ans.append(z)
        r[z]-=1
    return "".join(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()