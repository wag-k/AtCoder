# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:19:11 2018

@author: Owner
"""

import collections
import scipy.misc

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

N, M = map(int, input().split())

primeM = prime_decomposition(M)
factors = collections.Counter(primeM)

num_pattern = 1;

fact_max = M//N


print(factors)