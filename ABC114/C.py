# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:06:49 2018

@author: Owner
"""

import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter

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
"""

N = int(input())

if N < 357:
    print(0)
    sys.exit()

ans_c = 0
num753 = 0
next_flag = False 
for n in range(357, N+1):
    next_flag = False
    nstr = str(n)
    
    if len(nstr) != sum(nstr.count(c) for c in '753'):
        continue        
    
    if all(nstr.count(c) for c in '753'):
            num753 = num753 + 1
print(num753)


