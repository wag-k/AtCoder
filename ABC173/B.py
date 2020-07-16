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

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
"""


N=int(input())
S = [input() for n in range(N)]
s_counter = collections.Counter(S)
def main():
    cases = ["AC", "WA", "TLE", "RE"]
    for case in cases:
        cnt = 0
        if case in s_counter.keys():
            cnt =s_counter[case]
        print(case+" x "+str(cnt))
        
    return
    

if __name__ == '__main__':
    main()
