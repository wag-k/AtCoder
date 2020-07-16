# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:24:29 2018

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
"""


N = int(input())
S = ""
T = ""
for n in range(N):
    S = input()
    if S == "Mon":      
        T = "Tue"
    elif S == "Tue":
        T = "Wed"
    elif S == "Wed":
        T = "Thu"
    elif S == "Thu":
        T = "Fri"
    elif S == "Fri":
        T = "Sat"
    elif S == "Sat":
        T = "Sun"
    elif S == "Sun":
        T = "Mon"
    print(T)
    
