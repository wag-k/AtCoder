# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:52:46 2019

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

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
    
all(nstr.count(c) for c in '753')

ABT = zip(A, B, totAB)
result = 0
# itemgetterには何番目の配列をキーにしたいか渡します
sorted(ABT,key=itemgetter(2))
#A, B, totAB = zip(*ABT)

A.sort(reverse=True)

(x >> i) & 1

"""


N, M = map(int, input().split())
A = [0]*M
A[:] = map(int, input().split())
A.sort(reverse=False)

numM = [2, 5, 5, 4, 5, 6, 3, 7, 6]
useM = []
for a in A:
    useM.append(numM[a-1])

print(useM)

AM = zip(A, useM)
AM = sorted(AM,key=itemgetter(1))
A, useM = zip(*AM)
n = 0
num_useM = [0]*len(useM)
while True:
    num_useM[n] = N // useM[n]
    modulo = N % useM[n]
