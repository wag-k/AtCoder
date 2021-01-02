# -*- coding: utf-8 -*-

import bisect
import copy
import collections
import heapq
import itertools
import math
import numpy as np
from operator import itemgetter
import scipy.misc
import sys

"""
#### 入力例 ####
N, X = map(int, input().split())
x = list(map(int, input().split()))
S = [input() for n in range(N)]
P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
"""


N=int(input())
c = list(map(str, input()))

def main():
    cnt = collections.Counter(c)
    nr = cnt["R"]
    res = 0
    for n in range(nr):
        if(c[n]=="W"):
            res+=1
    print(res)
    return
    

if __name__ == '__main__':
    main()
