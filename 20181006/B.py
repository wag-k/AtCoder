# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:23:15 2018

@author: Owner
"""

import collections
import sys
import numpy as np
from operator import itemgetter

N, T = map(int, input().split())
c = [0]*N
t = [0]*N
ct = [[0, 0]]*N

for i in range(N):
    c[i], t[i] = map(int, input().split())
    ct[i]= [c[i], t[i]]

ct.sort(key=itemgetter(0), reverse=False)
for i in range(N):
    if ct[i][1] <= T:
        print(ct[i][0])
        sys.exit()
print("TLE")