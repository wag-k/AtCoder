# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:36:29 2018

@author: Owner
"""

import collections
import sys
import numpy as np
from operator import itemgetter

N = int(input())
x = [0]*N
y = [0]*N
h = [0]*N
xyh = [[0, 0, 0]]*N

h = 0
Cxy = [0, 0] 

for i in range(N):
    x[i], y[i], h[i] = map(int, input().split())
    xyh[i]= [x[i], y[i], h[i]]
    
xyh.sort(key=itemgetter(2), reverse=True)

for i in range(1,N):
    if xyh[i][2] == xyh[i-1][2]:
        
        if xyh[i][0] - xyh[i-1][0] > 0:
                
print(xyh)