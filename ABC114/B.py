# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:06:44 2018

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

"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
"""

S = input()

len_S = len(S)
s_list = []

for n in range(len_S):
    s_list.append(int(S[n]))

min753 = 10000

for n in range(len_S-2):
    temp_diff = abs(100*s_list[n] + 10*s_list[n+1] + s_list[n+2] - 753)
    if temp_diff < min753:
        min753 = temp_diff
        if min753 == 0:
            break
        

print(min753)
  
