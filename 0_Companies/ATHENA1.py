# Athena Health Preliminary Test - I

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def getTime(s):
    s,ans='A'+s,0
    for z in range(0,len(s)-1):
        p1,p2=ord(s[z+1])-64,ord(s[z])-64
        ans+=min(min(p1,p2)+26-max(p1,p2),abs(p1-p2))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getTime(s)

    fptr.write(str(result) + '\n')

    fptr.close()
