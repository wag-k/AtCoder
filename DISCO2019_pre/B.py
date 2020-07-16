# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:04:47 2019

@author: Owner
"""


N = int(input())

def first_q(x):
    return round(-x+1.5, 10)

def second_q(x):
    return round(x+0.5, 10)

def third_q(x):
    return round(-x+0.5, 10)

def fourth_q(x):
    return round(x-0.5, 10)

def judge(p):
    if p[1] <= first_q(p[0]) and p[1] <= second_q(p[0]) and p[1] >= third_q(p[0]) and p[1] >= fourth_q(p[0]):
        return True
    else:
        return False

lattice = [[(None, None)]*(N+1) for n in range(N+1)]
for n in range(N+1):
    for m in range(N+1):
        lattice[n][m] = (round(n/N, 10), round(m/N, 10))

res = 0
for n in range(N):
    for m in range(N):
        hantei = judge(lattice[n][m]) and judge(lattice[n+1][m]) and judge(lattice[n][m+1]) and judge(lattice[n+1][m+1])
        if hantei:
            res += 1
        #print(lattice[n][m], res, judge(lattice[n][m]), judge(lattice[n+1][m]), judge(lattice[n][m+1]), judge(lattice[n+1][m+1]), hantei)
print(res)
            