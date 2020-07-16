# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:51:18 2018

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
    
all(nstr.count(c) for c in '753')
"""

N, X = map(int, input().split())

burger = 'P'
if N == 0:
    print(1)
    sys.exit()

"""
for n in range(N):
    burger = 'B' + burger + 'P' +burger +'B'
burger4eat = burger[0:X]
print(burger)
"""
burger4eat = (X//6)*4 
if X%6 == 1:
    pass
elif X%6 == 2:
    burger4eat += 1
elif X%6 == 3:
    burger4eat += 2
elif X%6 == 4:
    burger4eat += 3
elif X%6 == 5:
    pass

print(burger4eat)