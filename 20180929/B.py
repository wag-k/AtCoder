# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:02:39 2018

@author: Owner
"""

    
import sys
    
n = input()
num = list(n)
n100 = num[0]
n10 = num[1]
n1 = num[2]
if (num[0] == num[1]) and (num[0] == num[2]):
    print(n)
    sys.exit()

if int(n) < int(n100)*100 + int(n100)*10 + int(n100):
    print(int(n100)*100 + int(n100)*10 + int(n100))

if int(n) > int(n100)*100 + int(n100)*10 + int(n100):
    print((int(n100)+1)*100 + (int(n100)+1)*10 + (int(n100)+1))
    