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
import bisect

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

def find_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())

    
all(nstr.count(c) for c in '753')

# 複数配列を並び替え
ABT = zip(A, B, totAB)
result = 0
# itemgetterには何番目の配列をキーにしたいか渡します
sorted(ABT,key=itemgetter(2))
A, B, totAB = zip(*ABT)
A.sort(reverse=True)

# 2進数のbit判定
(x >> i) & 1

# dp最小化問題
dp = [np.inf]*N
for n in range(N):
    if n == 0:
        dp[n] = 0
    else:
        for k in range(1,K+1):
            if n-k >= 0:
                dp[n] = min(dp[n], dp[n-k] + abs(h[n]-h[n-k]))
            else:
                break

"""

N = int(input())

b = [0]*N
b[:] = map(int, input().split())
if find_index(b, 1) == False:
    print(-1)
    sys.exit()
    
a = []
bs=copy.deepcopy(b)
bs.sort()
opn = [1]
clsd =[]
print(bs)
while a == b:
    clsd =opn.pop[0]
    
    break    
        
        
        