# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:02:43 2018

@author: Owner
"""

import collections
import sys

n = input()
n = int(n)
v = [0]*int(n)
v[:] = map(int, input().split())
#print(n)
#print(v)
v_o = [0]*int((n/2))
v_e = [0]*int((n/2))
for i in range(n):
    if i%2 == 0:
        v_o[i//2] = v[i]
    else:
        v_e[i//2] = v[i]

cnt_o = collections.Counter(v_o).most_common(2)
#print(cnt_o[0][1])
collections.Counter(v_e).most_common(1)
cnt_e = collections.Counter(v_e).most_common(2)
#print(cnt_e[0][1])

if cnt_o[0][0] == cnt_e[0][0]:
    if (cnt_o[0][1] == n//2) and (cnt_e[0][1] == n//2):
        print(n//2)
        sys.exit()
    if cnt_o[0][1] >= cnt_e[0][1]:
        n_min = n -cnt_o[0][1] - cnt_e[1][1]
        if (n_min > n -cnt_o[1][1] - cnt_e[0][1]):
            n_min = n -cnt_o[1][1] - cnt_e[0][1]
        print(n_min)
        sys.exit()
    elif cnt_o[0][1] < cnt_e[0][1]:
        n_min = n -cnt_o[1][1] - cnt_e[0][1]
        if (n_min > n -cnt_o[0][1] - cnt_e[1][1]):
            n_min = n -cnt_o[0][1] - cnt_e[1][1]
        print(n_min)
        sys.exit()
else:
    n_min = n -cnt_o[0][1] - cnt_e[0][1]
    print(n_min)
    sys.exit()