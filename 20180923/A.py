# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:58:23 2018

@author: Owner
"""

# 整数の入力
A, B, C = map(int, input().split())

tmp_max = 10*A + B + C 

if tmp_max < 10*B + C +A:
    tmp_max = 10*B + C +A

if tmp_max < 10*C + A +B:
    tmp_max = 10*C + A +B

# 出力
print("{}".format(tmp_max))