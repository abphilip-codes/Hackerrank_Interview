# https://www.hackerrank.com/challenges/crossword-puzzle/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def p(char, w_map, words, spaces):
    if not len(words): return w_map
    s = spaces[0]
    for w in words:
        if (len(w)!=len(s)): continue
        done,r = True,[]
        for z,(y,x) in enumerate(s):
            if (w_map[y][x]!=char and w_map[y][x]!=w[z]): done = False
            elif (w_map[y][x]==char):
                r.append((y,x))
                w_map[y][x] = w[z]
        if done:
            n = deepcopy(words)
            n.remove(w)
            m = p(char,deepcopy(w_map),n,spaces[1:])
            if (m!=[]): return m
            else:
                for (y,x) in r: w_map[y][x] = char
    return []

def crosswordPuzzle(crossword, words):
    cs = set(crossword[0])
    cs.remove('-')
    char,words,spaces,f = list(cs)[0],words.split(';'),[],[[''] * 10 for _ in range(10)]

    for y in range(10):
        for x in range(10):
            if crossword[y][x]==char or f[y][x]=='vh': continue
            if (x<9 and ('h' not in f[y][x]) and crossword[y][x+1]=='-'):
                s,i = [],0
                while (x+i)<10:
                    if crossword[y][x+i]=='-':
                        f[y][x+i]+='h'
                        s.append((y,x+i))
                        i+=1
                    else: break
                spaces.append(s)
            if (y<9 and ('v' not in f[y][x]) and crossword[y+1][x]=='-'):
                s,i = [],0
                while (y+i)<10:
                    if crossword[y+i][x]=='-':
                        f[y+i][x]+='v'
                        s.append((y+i,x))
                        i+=1
                    else: break
                spaces.append(s)
    w = [[char]*10 for _ in range(10)]
    ans = p(char, w, words, spaces)
    return [''.join(z) for z in ans]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()