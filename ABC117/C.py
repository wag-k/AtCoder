# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:43:36 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:47:58 2019

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

"""

N, M = map(int, input().split())

X = [0]*M
X[:] = map(int, input().split())

if N >= M:
    print(0)
    sys.exit()
else:
    pass

X.sort()

if N == 1:
    print(X[M-1]-X[0])
    sys.exit()
else:
    pass

dX = [0]*(M-1)
for m in range(M-1):
    dX[m] = X[m+1] - X[m]
dX = np.array(dX)
dX_rank = dX.argsort()[::-1]

X_div = dX_rank[0:N-1]
X_div.sort()
result =0
cnt = 0
last_idx = 0

#print(X_div)
for nx in X_div:
    if cnt == 0:
        result = result + X[nx]-X[0]
        last_idx = nx
        cnt =+ 1         
    else:
        result = result + X[nx] - X[last_idx+1]
        last_idx = nx
    #print(result)
#print(X[-1], X[last_idx+1])
result = result + X[-1] - X[last_idx+1]

print(result)