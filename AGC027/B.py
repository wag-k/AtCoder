# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 06:43:30 2018

@author: Owner
"""


N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

x.sort(reverse = True)

Energy_tot = 0
n_Trash = 0
flag_back = True
for n in range(N):
    if flag_back:
        Energy_tot += x[n]*(0 + 1)**2 + X
        n_Trash += 1
    if n == N-1:
        Energy_tot += x[n]*(n_Trash +1)**2 +X
        break
    Energy_tot += (x[n] - x[n+1])*(n_Trash + 1)**2
    if n < N-2:
        Energy_pass = x[n+1]*(n_Trash + 1)**2 + X + x[n+1]*(0 + 1)**2 + X + (x[n+1]-x[n+2])*(1 + 1)**2
        Energy_pick = X + (x[n+1]-x[n+2])*(n_Trash + 1 + 1)**2
        if Energy_pass < Energy_pick:
            Energy_tot += x[n+1]*(n_Trash + 1)**2 + X
            n_Trash = 0
            flag_back = True
        else:
            Energy_tot += X
            n_Trash += 1
            flag_back = False
    else:
        Energy_pass = x[n+1]*(n_Trash + 1)**2 + X + x[n+1]*(0 + 1)**2 + X + x[n+1]*(1 + 1)**2
        Energy_pick = X + x[n+1]*(n_Trash + 1 + 1)**2
        if Energy_pass < Energy_pick:
            Energy_tot += x[n+1]*(n_Trash + 1)**2 + X
            n_Trash = 0
            flag_back = True
        else:
            Energy_tot += X
            n_Trash += 1
            flag_back = False
print(Energy_tot)


