# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:51:13 2018

@author: Owner
"""

import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(int(i))
    i += 1
  if n > 1:
    table.append(int(n))
  return table   

def digit(i):
    if i > 0:
        return digit(i//10) + [i%10]
    else:
        return []

"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
    
all(nstr.count(c) for c in '753')
"""
N, K = map(int, input().split())


h = [0]*N
for n in range(N):
    h[n] = int(input())

h.sort()
diff_min = math.pow(10, 9)
diff_min = 10**9
#print(h)
for i in range(len(h)-K+1):
    #print(h[i], h[i+K-1])
    temp_diff = h[i+K-1] - h[i]
    
    if diff_min > temp_diff:
        diff_min = temp_diff
    if diff_min == 0:
        break
"""
for l in list(itertools.combinations(h,K)):
    
    temp_diff = l[np.argmax(l)] - l[np.argmin(l)]
    if diff_min > temp_diff:
        diff_min = temp_diff
    if diff_min == 0:
        break
"""     
print(diff_min)