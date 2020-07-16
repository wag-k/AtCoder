# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:47:32 2019

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
"""

N = int(input())

A = [0]*N
B = [0]*N
totAB = [0]*N
for n in range(N):
    A[n], B[n] = map(int, input().split())
    totAB[n] = A[n] + B[n]

ABT = zip(A, B, totAB)
result = 0
# itemgetterには何番目の配列をキーにしたいか渡します
sorted(ABT,key=itemgetter(2))
#A, B, totAB = zip(*ABT)
print(ABT)
totAB = ABT[2]
"""
while len(A) != 0:
    iT = totAB.index(max(totAB))
    if n % 2 == 0:
        result += A.pop(iT)
        del B[iT]
        del totAB[iT]
    else:
        result -= B.pop(iT)
        del A[iT]
        del totAB[iT]
    n +=1    
"""
resultA = sum(totAB[1::2])

resultB = sum(totAB[0::2]) 
result = resultA- resultB
print(result)
