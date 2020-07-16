# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:58:39 2018

@author: Owner
"""
import sys

S = input()
T = input()

len_S = len(S)
S_Converted = S
for i in range (len(S)):
    tmp_S = S_Converted[i]
    tmp_T = T[i]
    if tmp_S == tmp_T:
        continue
    S_Converted = list(S_Converted) 
    list_indexT = [j for j, tmp_SC in enumerate(S_Converted) if tmp_SC == tmp_T]
    if (not list_indexT == []) and (list_indexT[0] < i):
        print('No')
        sys.exit()
    S_Converted = ''.join(S_Converted)
    S_Converted = S_Converted.replace(tmp_S, tmp_T)
    S_Converted = list(S_Converted) 
    for li in list_indexT:
        if li == i:
            continue
        else:
            S_Converted[li] = tmp_S
    #print(''.join(S_Converted))
    
S_Converted = ''.join(S_Converted)

if S_Converted == T:
    print('Yes')
else:
    print('No')

    