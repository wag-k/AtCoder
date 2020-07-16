# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:53:12 2019

@author: Owner
"""
import numpy as np
import sys
import collections
import scipy.misc
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

x = list(map(int, input().split()))

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())

# 多次元配列の宣言（あとでintにすること。）（タプルにすること。）
dp = np.zeros((N+1, 4,4,4))
    
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
# 累積和
add = 1 # 問題によって決まる
res = 0
sums = [0]*(len(nums)+1)
for i in range(len(nums)):
    sums[i+1] = sums[i] + nums[i]
for i in range(0, len(nums), 2):
    left = i
    right = min(i+add, len(nums))
    tmp = sums[right] - sums[left]
    res = max(tmp, res)

#２分探索
li, ri = bisect.bisect_left(p_ac, l[i]-1), bisect.bisect_right(p_ac, r[i]-1)    

#ソート関数
org_list = [3, 1, 4, 5, 2]
new_list = sorted(org_list)
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [1, 2, 3, 4, 5]

#Distance Transformation
    for h in range(0,H):
        for w in range(0,W):
            if h == 0 and w == 0:
                pass
            elif h == 0:
                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h-1][W-w]+1)
            elif w == 0:   
                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1)
            else:
                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1, D[H-h-1][W-w]+1, D[H-h][W-w]+2)
            d_max = max(D[H-h-1][W-w-1], d_max)

"""

N, M = list(map(int, input().split()))
X = [0]*M
Y = [0]*M
Z = [0]*M

for m in range(M):
    X[m], Y[m], Z[m] = map(int, input().split())


def main(): 
    uf = UnionFind(N)
    for m in range(M):
        uf.union(X[m]-1, Y[m]-1)
    num = set()
    for n in range(N):
        num.add(uf.find(n))        
        
    print(len(num))
                
                
if __name__ == '__main__':
    main()
