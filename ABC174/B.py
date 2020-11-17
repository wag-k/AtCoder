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

N, D = map(int, input().split())
X = [0]*N
Y = [0]*N
for n in range(N):
    X[n], Y[n] = map(int, input().split())


def main():
    res = 0
    for n in range(N):
        r = math.sqrt(X[n]**2+Y[n]**2)
        if r <= D:
            res += 1
    print(res)
    return
    

if __name__ == '__main__':
    main()
