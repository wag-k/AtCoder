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
A = list(map(int, input().split()))

def main():
    A.sort(reverse=True)
    dq = collections.deque(A)
    now = dq.popleft()
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, (-now, now))    
    ans = 0
    for n in range(1,N):
        ans += heapq.heappop(hq)[1]
        now = dq.popleft()
        heapq.heappush(hq, (-now, now))
        heapq.heappush(hq, (-now, now))
    print(ans)
    return
    

if __name__ == '__main__':
    main()
