# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:52:23 2019

@author: Owner
"""

import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools
import copy

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
    
def getNearestValueIndex(list, num):
    """
    概要: リストからある値に最も近い値のインデックスを取得する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return idx

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
N = int(input())

h = [0]*N
h[:] = map(int, input().split())

h = np.array(h)

cnt = 0
while np.sum(h ==0) != N:
    if np.sum(h ==0) == 0:        
        h = h-1
        cnt +=1
    else:
        r=N-1
        for n in range(N-1):
            if h[n] == 0 and h[n+1] !=0:
                l = n+1
            elif h[0] != 0:
                l = 0
            else:
                pass
            if h[n] != 0 and h[n+1] == 0:
                r = n
                break
        for x in range(l, r+1):
            h[x] = h[x] -1
        cnt +=1
print(cnt)
            
            
            
        
            
