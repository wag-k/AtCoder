# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:18:19 2018

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


N, M = map(int, input().split())
P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
city_list = [[0, 0, 0, 0, 0]]*M
for m in range(M):
    city_list[m] = [P[m], Y[m], 0, 0, m]
city_list.sort()
i = 1
city_id = [0]*M
cnt = 1
for m in range(M):
    if city_list[m][0] == i:
        city_id[m] = cnt
        cnt += 1
    else:
        i += 1
        cnt = 1
        city_id[m] = cnt
        cnt += 1
    city_list[m][2] = city_id[m]
    city_list[m][3] = int(math.log10(city_list[m][0]) + 1)    
    
city_list.sort(key=itemgetter(4), reverse=False)
ID = ["0"]*M
for m in range(M):
    tmpID = 10**6*city_list[m][0]+city_list[m][2]
    ID[m] = "0"*(6-city_list[m][3])  + str(tmpID)
    print(ID[m])