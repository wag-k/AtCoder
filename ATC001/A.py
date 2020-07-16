# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:16:09 2019

@author: Owner
"""

from collections import deque

H, W = map(int, input().split())

maze = []
        
S = deque()

for h in range(H):
    maze.append(input())

#start
for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            S.append((h, w))
            break
#print("S: ", S)
#print("O: ", O)
#print("start")
def dfs():
    while len(S) != 0:
        h, w = S.pop()
        if maze[h][w] == "g":
            return "Yes"
        
        maze[h] = maze[h][:w]+"#"+maze[h][w+1:]
        if 0 <= h-1:
            if maze[h-1][w] != "#":
                S.append((h-1, w))
        if h+1 <= H-1:
            if maze[h+1][w] != "#":
                S.append((h+1, w))
        if 0 <= w-1:
            if maze[h][w-1] != "#":
                S.append((h, w-1))
        if w+1 <= W-1:
            if maze[h][w+1] != "#":
                S.append((h, w+1))
        #print("S: ", S)
        #print(maze)
        
    return "No"
            

print(dfs())