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


X, K, D = map(int, input().split())

def main():
    availableDist = K*D
    absX = abs(X)
    if absX - availableDist >= 0:
        return print(absX - availableDist)
    else:
        if (K - absX//D)%2 == 1:
            return print(abs(absX%D-D))
        else:
            return print(absX%D)

if __name__ == '__main__':
    main()
