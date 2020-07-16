# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:08:54 2018

@author: Owner
"""

import time
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
t_strt = time.time() 

factors = collections.Counter(prime_decomposition(M))
t_elps = time.time()
#print(f"{t_elps - t_strt} [sec]")
num_pattern = 1;

for exponent in factors.values():
    tmp_num_pattern = scipy.misc.comb(exponent + N -1, N-1, exact = True) 
    num_pattern = num_pattern * int(tmp_num_pattern)
    
print(num_pattern%(10**9+7))

t_elps = time.time()
#print(f"{t_elps - t_strt} [sec]")