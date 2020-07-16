# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:58:17 2019

@author: Owner
"""

K, S = map(int, input().split())

cnt = 0

for x in range(K+1):
    for y in range(K+1):
        if 0 <= S-(x+y) and S-(x+y)<=K :
            cnt+=1
print(cnt)