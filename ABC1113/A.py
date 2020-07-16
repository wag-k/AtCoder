# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:57:34 2018

@author: Owner
"""


import collections
import scipy.misc
import sys
import numpy as np
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

"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())
"""


X, Y = map(int, input().split())
print(X + int(Y/2))