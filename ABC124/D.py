# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:53:12 2019

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
"""

N, K = map(int, input().split())
S = input()
def main():
    now = 1
    cnt = 0
    nums = []
    for i in range(N):
        if S[i] == str(now):
            cnt += 1
        else:
            nums.append(cnt);
            now = 1-now
            cnt = 1
    if cnt != 0:
        nums.append(cnt)
    if len(nums)%2 ==0:
        nums.append(0)
    add = 2*K + 1
    res = 0
    # 累積和
    sums = [0]*(len(nums)+1)
    for i in range(len(nums)):
        sums[i+1] = sums[i] + nums[i]
    for i in range(0, len(nums), 2):
        left = i
        right = min(i+add, len(nums))
        tmp = sums[right] - sums[left]
        res = max(tmp, res)
    """
    # 尺取り法
    # ループの外にleft , right
    left = 0
    right = 0
    tmp= 0 # [left, right) のsum
    for i in range(0, len(nums), 2):
        # 次のleft, right を計算
        nextLeft = i
        nextRight = min(i+add, len(nums))
        # 左端を計算
        while (nextLeft > left):
            tmp -= nums[left]
            left += 1
        
        # 右端を計算
        while (nextRight > right):
            tmp += nums[right]
            right +=1
        res = max(tmp, res)
    """
    print(res)
 
if __name__ == '__main__':
    main()