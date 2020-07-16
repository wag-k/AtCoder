# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:47:47 2019
 
@author: Owner
"""
 
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:53:12 2019
 
@author: Owner
"""
 
from operator import itemgetter
import itertools
import collections
import bisect
 
N, M = list(map(int, input().split()))
 
A = list(map(int, input().split()))
A.sort()

A = collections.deque(A)

BC = [(0, 0)]*M
for m in range(M):
    BC[m] = tuple(map(int, input().split()))
BC.sort(key=itemgetter(1), reverse = True)
 
def main(): 
    #print(BC)
    res = 0
    for i in range(M):
        idx = 0         
        idx = bisect.bisect_left(A, BC[i][1])
        if idx == 0:
            break
        else:
            less =min(idx, BC[i][0])
            for n in range(less):
                A.popleft()
            res += BC[i][1]*less
 
    print(res+sum(A))
                
                
                
            
            
                
 
    
if __name__ == '__main__':
    main()