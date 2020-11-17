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


K=int(input())

def main():
    a = np.zeros((10**6+1))
    a[0] = 7 % K
    if(a[0] == 0):
        return print(1)
    for k in range(1,K):
        a[k] = (10*a[k-1]+7)%K
        if(a[k] == 0):
            return print(k+1)

    return print(-1)
    

if __name__ == '__main__':
    main()
