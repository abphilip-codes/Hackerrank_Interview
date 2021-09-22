# https://www.hackerrank.com/challenges/decibinary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
from collections import defaultdict, Counter

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

class Decibinary:
    def __init__(self):
        self.COUNT = [[1, 1]]
        self.cum_sums = [1]
        self.min_dig = [0] 
        for p in range(20): self.min_dig.append(9 * 2 ** p + self.min_dig[-1])

    def decibinaryNumbers(self, x):
        if x > self.cum_sums[-1]:
            n = len(self.COUNT)
            num=x
            while self.cum_sums[-1] < num:
                min_digits = bisect.bisect_left(self.min_dig, n)
                max_digits = math.floor(math.log(n, 2)) + 1 

                self.COUNT.append([0] * (max_digits + 1))
                for m in range(min_digits, max_digits + 1):
                    self.COUNT[n][m] = self.COUNT[n][m - 1]
                    for d in range(1, 10):
                        remainder = n - d * 2 ** (m - 1)
                        if remainder >= 0:
                            self.COUNT[n][m] += self.COUNT[remainder][min(m - 1, len(self.COUNT[remainder]) - 1)] 
                        else: 
                            break
                self.cum_sums.append(self.cum_sums[-1] + self.COUNT[-1][-1])
                n += 1    
            
        if x == 1: return 0
        n = bisect.bisect_left(self.cum_sums, x)
        n_rem = x - self.cum_sums[n - 1]
        m = bisect.bisect_left(self.COUNT[n], n_rem)
        m_rem = n_rem - self.COUNT[n][m - 1]
        
        return int(self.reconstruct(n, m, m_rem)) 


    def reconstruct(self, n, m, rem, partial=0):
        if m == 1: return partial + n

        skipped = 0
        for k in range(not partial, 10):
            dig_val = k * 2 ** (m - 1)
            smaller = n - dig_val
            s_m = min(len(self.COUNT[smaller]) - 1, m - 1)
            skipped += self.COUNT[smaller][s_m]
            if skipped >= rem:
                partial += k * 10 ** (m-1) #math.pow(10,(m - 1))
                new_rem = rem - (skipped - self.COUNT[smaller][s_m])
                return self.reconstruct(smaller, s_m, new_rem, partial) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    db = Decibinary()

    for q_itr in range(q):
        x = int(input().strip())

        result = db.decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()