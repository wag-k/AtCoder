# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:10:04 2018

@author: Owner
"""

# 整数の入力
N, M, X, Y = map(int, input().split())
x = map(int, input().split())
y = map(int, input().split())

x_max = max(x)
y_min = min(y)

flag_war = True

for z in range(X+1, Y+1):
    if x_max < z:
        if y_min >= z:
            print('No War')
            flag_war = False
            break
        else:
            continue
    else:
        continue
if flag_war == True:
    print('War')
