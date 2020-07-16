# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:42:51 2018

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

L, N = map(int, input().split())

X = [0]*N
for n in range(N):
    X[n] = int(input())

lmax = 0
for n in range(2**N):
    p_now = 0
    l=0
    pat = format(n, "b").zfill(N)
    X_cp = X[:]
    print(pat)
    for pat_now in pat:
        #print(pat_now)
        #print(X_cp)
        if int(pat_now):              
            if p_now < X_cp[0]:
                l =l + X_cp[0] - p_now
                p_now = X_cp.pop(0)
            else:
                l += L - p_now + X_cp[0]
                p_now = X_cp.pop(0)
        else:
            if p_now < X_cp[-1]:
                l += p_now + L - X_cp[-1]
                p_now = X_cp.pop(-1)
            else:
                l += p_now - X_cp[-1]
                p_now = X_cp.pop(-1) 
    if lmax < l:
        lmax = l
    print(l)
print(lmax)