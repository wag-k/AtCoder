# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

import bisect

N, M = list(map(int, input().split()))
a = [0]*M
for m in range(M):
    a[m] = int(input())
a = set(a)
MOD = 10**9 + 7

def main(): 
    dp = [0]*(N+2)
    dp[0] = 1
    for n in range(1,N+1):
        if n ==1:
            if n in a:
                dp[n] = 0
            else:
                dp[n] += dp[n-1]
                
        else:                        
            if n in a:
                dp[n] = 0
            else:
                dp[n] += dp[n-2] + dp[n-1]
                
    #print(dp)
    print(dp[N]%MOD)
                
                
                
            
            
                

    
if __name__ == '__main__':
    main()
