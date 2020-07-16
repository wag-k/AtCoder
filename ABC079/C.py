# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:21:54 2019

@author: Owner
"""

S = input()

A = [int(S[0]), int(S[1]), int(S[2]), int(S[3])]

flg = [True, True, True]

def dfs(n, flg, goal):
    if goal == True:
        return True
    
    if n == 3:
        ops = ["+", "+", "+"]
        tot = A[0]
        for i in range(len(flg)):
            if flg[i]:
                tot += A[i+1]
            else:
                tot -= A[i+1]
                ops[i] = "-" 
        #print("Layer: "+str(n)+", Flags: "+str(flg)+", Total: "+str(tot))
                
        if tot == 7:
            print(str(A[0])+ops[0]+str(A[1])+ops[1]+str(A[2])+ops[2]+str(A[3])+"=7")
            return True
        else:
            return False
    #print("Layer: "+str(n)+", Flags: ", flg)
    flg1 = flg.copy()
    flg1[n] = True
    flg2 = flg.copy()
    flg2[n] = False
    
    goal = dfs(n+1, flg1, goal) or dfs(n+1, flg2, goal)
    
    return goal
    
dfs(0, flg, False)