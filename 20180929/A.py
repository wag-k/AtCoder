# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:02:44 2018

@author: Owner
"""

n = input()
num = list(n)
for i in range(len(num)):
    if num[i] == "1":
        num[i] = "9"
        continue
    if num[i] == "9":
        num[i] ="1"
        continue

num = ''.join(num)
print(int(num))