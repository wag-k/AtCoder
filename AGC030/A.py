# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:42:42 2018

@author: Owner
"""


import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools

#素因数を並べる
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
# 桁数を吐く
def digit(i):
    if i > 0:
        return digit(i//10) + [i%10]
    else:
        return []

A, B, C = map(int, input().split())
n_poison = 0
if A+B >= C:
    n_poison = C
else:
    n_poison = A+B+1
print(B+n_poison)
    
    