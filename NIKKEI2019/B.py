# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:47:18 2019

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
A = input()
B = input()
C = input()

result = 0

for n in range(N):
    if A[n] == B[n] and B[n] == C[n]:
        continue
    else:
        if A[n] == B[n] or B[n] == C[n] or C[n] == A[n]:
            result += 1
        else:
            result +=2
print(result)
                
            
