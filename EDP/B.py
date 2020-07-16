# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:22:35 2019

@author: Owner
"""
import numpy as np

N, K = map(int, input().split())

h = [0]*N
h[:] = map(int, input().split())

dp = [np.inf]*N

for n in range(N):
    if n == 0:
        dp[n] = 0
    else:
        for k in range(1,K+1):
            if n-k >= 0:
                dp[n] = min(dp[n], dp[n-k] + abs(h[n]-h[n-k]))
            else:
                break
    #print(dp)
print(dp[N-1])