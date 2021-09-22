# https://www.hackerrank.com/challenges/decibinary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def decibinaryNumbers(x):
    my_dict={}
    result=[]
    for i in range(0,100000):
        deci=db_value(i)
        my_dict.update({i:deci})
    
    temp=sorted (my_dict.items(),key=lambda kv:(kv[1],kv[0]))

    return(temp[x-1][0])        
        
def db_value(num):
    n=0
    deci=0
    while(num>0):
        rem=num%10
        deci+=rem*(2**n)
        num=num//10
        n+=1
    return deci

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()