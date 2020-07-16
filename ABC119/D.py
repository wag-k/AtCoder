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

A, B, Q = map(int, input().split())

s = [0]*A
for n in range(A):
    s[n] = int(input())
t = [0]*B
for n in range(B):
    t[n] = int(input())
x = [0]*Q
for i in range(Q):
    x[i] = int(input())

print('ans')
for i in range(Q):
    nearA = getNearestValueIndex(s, x[i])
    nearB = getNearestValueIndex(t, x[i])
    print(nearA, nearB)
    if nearB == 0 and s[nearA] <= x[i] and t[nearB] >= x[i]:
        print('p1')
        print(min(abs(t[nearB]-s[nearA]), abs(s[nearA+1] -x[i])))
        
        continue
    elif nearA == 0 and s[nearA] >= x[i] and t[nearB] <= x[i]:
        print('p2')
        print(min(abs(s[nearA]-t[nearB]), abs(t[nearB+1]-x[i]) ))
        continue
    elif nearA == 0 and s[nearA] >= x[i] and nearB ==0 and t[nearB] >= x[i]:
        print('p3')
        print(max(abs(s[nearA]-x[i]), abs(t[nearB]-x[i])))
        continue
    elif nearA == A-1 and s[nearA] <= x[i] and nearB ==B-1 and t[nearB] <= x[i]:
        print('p4')
        print(max(abs(s[nearA]-x[i]), abs(t[nearB]-x[i])))
        continue
    elif nearA == A-1 and s[nearA] <= x[i] and t[nearB] >= x[i]:
        print('p5')
        print(min(abs(t[nearB-1]-x[i]), abs(s[nearA]-x[i])+abs(t[nearB]-s[nearA])))
        continue
    elif nearB == B-1 and s[nearA] >= x[i] and t[nearB] <= x[i]:
        print('p6')
        print(min(abs(s[nearA-1]-x[i]), abs(t[nearB]-x[i])+abs(s[nearA]-t[nearB])))
        continue

    if s[nearA] <= x[i] and t[nearB] <= x[i]:
        print(max(abs(s[nearA]-x[i]), abs(t[nearB]-x[i])))
    elif s[nearA] >= x[i] and t[nearB] >= x[i]:
        print(max(abs(s[nearA]-x[i]), abs(t[nearB]-x[i])))
    elif s[nearA] <= x[i] and t[nearB] >= x[i]:
        print(min( abs(t[nearB-1]-x[i]), abs(t[nearB]-s[nearA]), abs(s[nearA+1]-x[i]) ))
    elif s[nearA] >= x[i] and t[nearB] <= x[i]:
        print(min( abs(s[nearA-1]-x[i]), abs(s[nearA]-t[nearB]), abs(t[nearB+1]-x[i]) ))
