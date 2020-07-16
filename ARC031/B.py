# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:06:15 2019

@author: Owner
"""

from collections import deque

A = []
N = 10

for n in range(10):
    A.append(input())


def dfs():
    
    for h0 in range(N):
        for w0 in range(N):
            O = deque([(h0, w0)])
            C = A.copy()
            while len(O) != 0:
                h, w = O.pop()
                C[h] = C[h][:w]+"x"+C[h][w+1:]
                if 0 <= h-1:
                    if C[h-1][w] == "o":
                        O.append((h-1, w))
                if h+1 <= N-1:
                    if C[h+1][w] == "o":
                        O.append((h+1, w))
                if 0 <= w-1:
                    if C[h][w-1] == "o":
                        O.append((h, w-1))
                if w+1 <= N-1:
                    if C[h][w+1] == "o":
                        O.append((h, w+1))
            #print(C)
            flg = True
            for h in range(N):
                if "o" in C[h]:
                    flg = False
                    break    
            if flg:
                return "YES"
            
    return "NO"
                

print(dfs())