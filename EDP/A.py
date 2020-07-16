# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:49:31 2019

@author: Owner
"""
import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools
import copy



N = int(input())

h = [0]*N
h[:] = map(int, input().split())

dp = [np.inf]*N

for n in range(N):
    if n == 0:
        dp[n] = 0
    elif n== 1:
        dp[n] = abs(h[n] - h[n-1])
    else:
        dp[n] = min(dp[n-2] + abs(h[n]-h[n-2]), dp[n-1] + abs(h[n]-h[n-1]))
    #print(dp)
print(dp[N-1])