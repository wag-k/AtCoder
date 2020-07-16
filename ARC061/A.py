# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:21:41 2019

@author: Owner
"""

from collections import deque

S = input()

lens = len(S)
    
def rec(i, cp, s, tot):
    if i == lens:
        print(s)
        tmp = list(map(int, s.split("+")))
        return sum(tmp)
    
    tot += rec(i+1, cp+1, s[:i+cp]+"+"+s[i+cp:], tot) + rec(i+1, cp, s, tot)
    print("Layer: "+str(i)+", Total: "+str(tot))
    return tot
    

def main():    
    return print(rec(1, 0, S, 0))
             
                
                
            
            
                

    
if __name__ == '__main__':
    main()