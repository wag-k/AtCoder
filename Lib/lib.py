# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

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
import heapq

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

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]
    

"""
# 入力あれこれ
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
            
            
#Bit DFS
S = input()

A = [int(S[0]), int(S[1]), int(S[2]), int(S[3])]

flg = [True, True, True]

def dfs(n, flg, goal):
    if goal == True:
        return True
    
    if n == 3:
        ops = ["+", "+", "+"]
        tot = A[0]
        for i in range(len(flg)):
            if flg[i]:
                tot += A[i+1]
            else:
                tot -= A[i+1]
                ops[i] = "-" 
        #print("Layer: "+str(n)+", Flags: "+str(flg)+", Total: "+str(tot))
                
        if tot == 7:
            print(str(A[0])+ops[0]+str(A[1])+ops[1]+str(A[2])+ops[2]+str(A[3])+"=7")
            return True
        else:
            return False
    #print("Layer: "+str(n)+", Flags: ", flg)
    flg1 = flg.copy()
    flg1[n] = True
    flg2 = flg.copy()
    flg2[n] = False
    
    goal = dfs(n+1, flg1, goal) or dfs(n+1, flg2, goal)
    
    return goal
    
dfs(0, flg, False)


#Maze BFS
from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
sx -= 1
sy -= 1
gy, gx = map(int, input().split())
gx -= 1
gy -= 1

maze = []
for r in range(R):
    maze.append(input())


def bfs():
    O = deque([(sx, sy, 0)])
    
    while len(O) != 0:
        x, y, cost= O.popleft()
        if x == gx and y == gy:
            return cost
        
        
        if 0 <= x-1:
            if maze[y][x-1] == ".":
                O.append((x-1, y, cost+1))                
                maze[y] = maze[y][:x-1]+"#"+maze[y][x:]
        if  x+1 <= C-1:
            if maze[y][x+1] == ".":
                O.append((x+1, y, cost+1))                
                maze[y] = maze[y][:x]+"#"+maze[y][x+1:]
        if 0 <= y-1:
            if maze[y-1][x] == ".":
                O.append((x, y-1, cost+1))                
                maze[y-1] = maze[y-1][:x]+"#"+maze[y-1][x+1:]
        if  y+1 <= R-1:
            if maze[y+1][x] == ".":
                O.append((x, y+1, cost+1))            
                maze[y+1] = maze[y+1][:x]+"#"+maze[y+1][x+1:]
        #print(maze)
        #print(cost)
        #print(O)
            
print(bfs())


# グラフの張り方
E = [[] for n in range(N)]

 
for m in range(M):
    e = list(map(int, input().split()))
    E[e[0]-1].append(e[1]-1)


"""


def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d
# cook your dish here
def dijkstra_back(s,t,n,w,cost):
    #sからtへの最短経路の経路復元
    prev = [s] * n #最短経路の直前の頂点
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
        
        for i in range(n):
            if d[i] > d[v] + cost[v][i]: 
                d[i] = d[v] + cost[v][i]
                prev[i] = v
        
    path = [t]
    while prev[t] != s:
        path.append(prev[t])
        prev[t] = prev[prev[t]]
    path.append(s)
    path = path[::-1]
    return path
"""
# ダイクストラのコストの張り方
N, M, L = list(map(int, input().split()))
cost = [[float("inf") for i in range(N)] for i in range(N)] 

#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
for m in range(M):
    x,y,z = map(int,input().split())
    cost[x-1][y-1] = z
    cost[y-1][x-1] = z
"""