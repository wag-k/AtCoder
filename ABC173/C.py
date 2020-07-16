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
C = [list(input()) for n in range(H)]
A = [list(map(int, input().split())) for n in range(H)]

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
"""


H, W, K = map(int, input().split())
C = [list(input()) for n in range(H)]

def main():
    C_ = np.array(C)
    row_list = collections.deque()
    for n in range(2**H):
        row_list.append([h for h in range(H) if not (n>>h) & 1])
    col_list = collections.deque()
    for n in range(2**W):
        col_list.append([w for w in range(W) if not (n>>w) & 1])
    buf_col_list = list(col_list)
    ans = 0
    while row_list:
        rows = row_list.pop()
        col_list = collections.deque(buf_col_list)
        while col_list:
            cols = col_list.pop()
            cnt = 0
            for h in rows:
                for w in cols:
                    if C_[h,w] == "#":
                        cnt+=1
            if cnt == K:
                ans+=1
    print(ans)
    return
    

if __name__ == '__main__':
    main()
