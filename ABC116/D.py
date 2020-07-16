# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:52:35 2019

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

N, K = map(int, input().split())

t = [0]*N
d = [0]*N
for n in range(N):
    t[n], d[n] = map(int, input().split())
a = [i for i in range(N)]
L = list(itertools.combinations(a,K))
result=0
for l in range(len(L)):
    tmp_t=[]
    oisisa = 0
    tmp_result = 0
    li = L[l]
    for idx in li:
        tmp_t.append(t[idx])
        oisisa += d[idx]
    
    X = collections.Counter(tmp_t)
    num_key = len(X.keys())
    
    tmp_result = num_key**2 + oisisa
    if tmp_result > result:
        result = tmp_result
print(result)
