# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

H, W = list(map(int, input().split()))
# 多次元配列の宣言（あとでintにすること。）（タプルにすること。）
A = [""]*H 
#INF = np.Inf
INF = 2000

#D = np.zeros((H+1, W+1))
D = [[0]*(W+1) for h in range(H+1)]

for h in range(H):
    A[h] = input()
    for w in range(W):
        if A[h][w] == '.':
            D[h][w] = 1           

def main(): 
    #G = np.zeros((H+1, W+1))
    #T = np.zeros((H+1, W+1)) # 自分以外横に何マスつながっているか
    #Y = np.zeros((H+1, W+1)) # 自分以外縦に何マスつながっているか
    T = [[0]*(W+1) for h in range(H+1)]
    Y = [[0]*(W+1) for h in range(H+1)]
    
    for h in range(H):
        cnt = 0
        for w in range(W):
            if D[h][w] == 0:
                cnt = 0
                continue
            else:
                Y[h][w] += cnt
                cnt+=1    
    for h in range(H):
        for w in reversed(range(W)):
            if D[h][w] == 0:
               continue
            else:
               Y[h][w] = max(Y[h][w], Y[h][w+1])                           
            
    for w in range(W):
        cnt = 0
        for h in range(H):
            if D[h][w] == 0:
                cnt = 0
                continue
            else:
                T[h][w] += cnt
                cnt+=1
    for w in range(W):
        for h in reversed(range(H)):
            if D[h][w] == 0:
                continue
            else:
                T[h][w] = max(T[h][w], T[h+1][w])
    #G = D+Y+T
    #res = np.amax(G)
    res = 0
    for w in range(W):
        for h in range(H):
            res = max(res, D[h][w]+Y[h][w]+T[h][w])
    print(int(res))
            
            
                

    
if __name__ == '__main__':
    main()
