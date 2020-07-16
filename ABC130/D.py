# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

import collections
from operator import itemgetter
import itertools
import copy
import bisect



N, K = list(map(int, input().split()))
a = list(map(int, input().split()))


def main(): 
    res = 0
    sums = [0]*(N+1)
    for n in range(1,N+1):
        sums [n] = sums[n-1] + a[n-1]
    for i in range(len(sums)):
        r = K + sums[i]
        ri = bisect.bisect_left(sums, r)
        if ri <= N:
            res += N-ri+1
        #print(i, r, ri, res)
        
    #print(sums)
    print(res)
                
                
                
            
            
                

    
if __name__ == '__main__':
    main()
