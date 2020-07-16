# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:44:00 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:43:41 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:42:51 2018

@author: Owner
"""

#import collections
#import scipy.misc
#import sys
import numpy as np
#import math
#from operator import itemgetter
#import itertools
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

N, Q = map(int, input().split())

A = [0]*N
A[:] = map(int, input().split())

X = [0]*Q
for q in range(Q):
    X[q] = int(input())


for q in range(Q):
    T =[]
    if X[q] <= A[0]:
        if N%2 == 0:
            t = sum(A[q/2-1:q])
        else:
            t = sum(A[q/2-2:q]) 
        print(t)
        continue
    elif X[q] >= A[-1]:
        
    tmpA = copy.deepcopy(A)
    while len(tmpA) != 0:
        T.append(tmpA.pop())
        if len(tmpA)!=0:
            tmpA.pop(getNearestValueIndex(tmpA, X[q]))
        else:
            pass
    print(sum(T))  
        