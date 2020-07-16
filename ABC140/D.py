# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

import numpy as np
import sys
import collections
import scipy.misc
import math
from operator import itemgetter
import itertools
import copy
import bisect
import heapq



N, K = list(map(int, input().split()))
S = input()
    
def main():
    res = N
    past = S[0]
    cnt = K
    cnt2= 0
    if N == 1:
        return print(0)
    flg = False
    for n in range(1, N):
        now = S[n]
        #print(past, now, res)
        if past == "R" and now == "L":
            #print(n, ": BAD")
            res -= 2
            flg = True
        if past == "L" and now == "R" and flg == True:
            if 0 < cnt:
                #print("reverse")
                res += 2
                cnt -= 1
                cnt2 += 1
            flg = False
        past = now
    
    if flg == True and 0 < cnt:
        res += 1
    #print("Reach edge: ", res)
    if S[0] == "L":
        #print(0, ": edge BAD")
        res -= 1
        if 0 < cnt and ("R" in S) :
            #print("reverse")
            res += 1
            cnt -= 1        
    if S[-1] == "R":
        res -= 1
        #print(N-1, ": edge BAD")
        
    return print(res)
                
                
                
            
            
                

    
if __name__ == '__main__':
    main()
