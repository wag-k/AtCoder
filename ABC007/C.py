# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:28:40 2019

@author: Owner
"""
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


