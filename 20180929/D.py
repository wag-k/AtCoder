# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:02:44 2018

@author: Owner

一番遠い点に行くアームを作り、その後分割していく
"""

import collections
import sys
import numpy as np
from operator import itemgetter

n = input()
n = int(n)
X = [0]*n
Y = [0]*n
L = [0]*n #len(path)
plot_list = [[0, 0, 0]]*n
m_max = 40
d = []

for i in range(n):
    X[i], Y[i] = map(int, input().split())
    L[i] = abs(X[i])+abs(Y[i])
    if i >= 1:
        if (L[i] % 2) != (L[i-1] % 2):
            print(-1)
            sys.exit()
    plot_list[i] = [X[i], Y[i], L[i]]
    
p_far = np.argmax(L)
plot_list.sort(key=itemgetter(2), reverse=True)

print(plot_list)

cmd_list = []
m = 0

for i in range(n):
    if m > 40:
        print(-1)
    tmp_plot = plot_list[i] 
    if i == 0:
        if np.sign(tmp_plot[0]) == 0:
            d.append(np.abs(tmp_plot[1]))
            m += 1
        else:
            d.append(np.abs(tmp_plot[0]))            
            m += 1
            if np.sign(tmp_plot[0]) == 0:
                pass
            else:
                d.append(np.abs(tmp_plot[1]))
                m += 1
        d.sort()
        continue
    if np.abs(tmp_plot[0]) in d:
        pass
    else:
        tmp_dm = d[m-1]
        d[m-1] = np.abs(tmp_dm - tmp_plot[0])
        d.append(np.abs(tmp_plot[0]))
        d.sort()
        if tmp_plot[0] != 0:
            m+=1
    if np.abs(tmp_plot[1]) in d:
        pass
    else:
        if (sum(d)-np.abs(tmp_plot[0])) == np.abs(tmp_plot[1]):
            pass
        else:            
            tmp_dm = d[m-1]
            d[m-1] = np.abs(tmp_dm - tmp_plot[1])
            for j in d:
                
            d.append(np.abs(tmp_plot[1]))            
            d.sort()
        if tmp_plot[1] !=0:
            m+=1
    d.sort()
print(d)
    