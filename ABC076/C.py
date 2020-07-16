# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 08:35:15 2019

@author: Owner
"""

from collections import deque

Sd = input()
T = input()
S = deque()

Sr = list(reversed(Sd))
Tr = list(reversed(T))

flg_match = True    
for i,s in enumerate(Sr):
    flg_match = True    
    for j,t in enumerate(Tr):
        if i+j >= len(Sr):
            flg_match = False
            break
        if t == Sr[i+j] or Sr[i+j] == "?":
            pass
        else:
            flg_match = False
            break
        #print(t, Sr[i+j], flg_match)
    if flg_match:
        S.appendleft(T)
        #print(Sd)
        break
    else:
        if s == "?":
            S.appendleft("a")
        else:
            S.appendleft(s)
#print(flg_match)
if not flg_match:
    print("UNRESTORABLE")
else:    
    S = "".join(list(S))
    S = Sd[:len(Sd)-len(S)]+S
    S = S.replace("?", "a")
    
    print(S)