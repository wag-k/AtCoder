# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:12:17 2019

@author: Owner
"""

from operator import itemgetter
import bisect

N, M = map(int, input().split())


ab = [(0, 0)]*M
for m in range(M):
    ab[m] = tuple(map(int, input().split()))

ab = tuple(sorted(ab, key = itemgetter(1)))

#print(ab)
x_rm = -1
res = 0
for m in range(M):
    if ab[m][0] < x_rm:
        continue
    else:
        x_rm = ab[m][1]
        res += 1
    
    
        

print(res)

