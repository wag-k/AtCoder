# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:43:56 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:43:41 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:42:51 2018

@author: Owner
"""

#import collections
#import scipy.misc
#import sys
import numpy as np
#import math
#from operator import itemgetter
#import itertools
#素因数を並べる
"""
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(int(i))
    i += 1
  if n > 1:
    table.append(int(n))
  return table   
# 桁数を吐く
def digit(i):
    if i > 0:
        return digit(i//10) + [i%10]
    else:
        return []
    
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
    
all(nstr.count(c) for c in '753')

def main():
    

if __name__ == '__main__':
    main()

"""

H, W = map(int, input().split())

S = [input() for h in range(H)] 


def main():
    l_opn = []
    l_cls = list(range(H*W))
    #print(l_cls)
    result = 0
    n=0
    h=0
    w=0
    nb=0
    nw=0
    flag_next = True
    while l_cls:
        cnt_opn = 0
        if flag_next:                
            l_opn.append(l_cls.pop(0))
            n = l_opn[0]
            h = n % H
            w = n // H
            if (S[h][w] == "#"):
                nb +=1
            else:
                nw +=1
            
        n = l_opn.pop(0)
        h = n % H
        w = n // H
                
        if (w > 0)  and (S[h][w-1] != S[h][w]):
            if (n-H) in l_cls:
                l_opn.append(l_cls.pop(l_cls.index(n-H)))
                if (S[h][w-1] == "#"):
                    nb +=1
                else:
                    nw +=1
                cnt_opn +=1
            else:
                pass
        else:
            pass
            
        if (h > 0) and (S[h-1][w] != S[h][w]):
            if (n-1) in l_cls:
                l_opn.append(l_cls.pop(l_cls.index(n-1)))
                if (S[h-1][w] == "#"):
                    nb +=1
                else:
                    nw +=1
                cnt_opn +=1         
            else:
                pass
        else:
            pass
        
        if (h < H-1) and (S[h+1][w] != S[h][w]):
            if (n+1) in l_cls:
                l_opn.append(l_cls.pop(l_cls.index(n+1)))
                if (S[h+1][w] == "#"):
                    nb +=1
                else:
                    nw +=1
                cnt_opn +=1  
            else:
                pass
        else:
            pass    
                
        if (w < W-1) and (S[h][w+1] != S[h][w]):
            if (n+H) in l_cls:
                l_opn.append(l_cls.pop(l_cls.index(n+H)))
                if (S[h][w+1] == "#"):
                    nb +=1
                else:
                    nw +=1
                cnt_opn +=1
            else:
                pass
        else:
            pass                  
        if cnt_opn == 0 and (not l_opn):
            result += nb*nw
            #print(result)
            n=0
            nb=0
            nw=0
            #print("cls: "+str(l_cls))
            l_opn = []
            flag_next = True
        else:
            
            #print("opn: "+str(l_opn))
            flag_next = False
            pass
    result += nb*nw    
    print(result)
if __name__ == '__main__':
    main()

