# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""

from operator import itemgetter


N = int(input())


AB = [(0, 0, 0)]*N
for n in range(N):
    a, b = list(map(int, input().split()))
    AB[n] = (a, b, b-a) 
AB = tuple(sorted(AB, key = itemgetter(1)))

    
def main():
    tot = 0
    for i, ab in enumerate(AB):
        if tot <= ab[2]:
            tot+=ab[0]
        else:
            return print("No")
        #print(ab, tot)
    print("Yes")
                
                
            
            
                

    
if __name__ == '__main__':
    main()
