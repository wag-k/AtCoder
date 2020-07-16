# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:55:15 2018

@author: Owner
"""

import sys
import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

N, M = map(int, input().split())
S = input()
T = input()

if S[0] != T[0]:
    print(-1)
    sys.exit()
lcm_NM = lcm(N, M)

tmp_L = lcm_NM

xn_index = [0]*(N)
xm_index = [0]*(M)  
xn_index[0] = 1
xm_index[0] = 1
for n in range(N):
    if n == 0:
        continue
    xn_index[n] = (n)*tmp_L//N+1
for m in range(1,M):
    if m == 0:
        continue
    xm_index[m] = (m)*tmp_L//M+1
n_set = set(xn_index)
m_set = set(xm_index)
matched_list = list(n_set & m_set)
if len(matched_list) == 1:
    pass
else:
    for k in matched_list:
        if (S[(k-1)*N//tmp_L]) == (T[(k-1)*M//tmp_L]):
            continue
        else:
            print(-1)
            sys.exit()
                    
L = tmp_L
print(L)
