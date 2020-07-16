# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:24:57 2019

@author: Owner
"""

import numpy as np
from operator import itemgetter

W = int(input())
N, K = map(int, input().split())

AB = [(0, 0)]*N

for n in range(N):
    AB[n] = tuple(map(int, input().split()))
    sorted(AB, key = itemgetter(1), reverse=True)

dp = np.zeros((N+1, W+1, K+1))

for i in range(N):
    for j in range(W):
        for k in range(K):
            if j < AB[i][0]:
                dp[i+1][j][k+1] = dp[i][j][k+1]
            else: 
                if dp[i][j][k] < dp[i][j-AB[i][0]][k] + AB[i][1]:
                    dp[i+1][j][k+1] = dp[i][j-AB[i][0]][k] + AB[i][1]
                    
                else:
                    dp[i+1][j][k+1] = dp[i][j][k+1]
print(int(np.amax(dp)))