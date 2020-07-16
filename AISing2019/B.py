# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:43:52 2019

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


import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools
#素因数を並べる
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
"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
    
all(nstr.count(c) for c in '753')
"""# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:43:41 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 18:42:51 2018

@author: Owner
"""

import collections
import scipy.misc
import sys
import numpy as np
import math
from operator import itemgetter
import itertools
#素因数を並べる
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
"""
N, X = map(int, input().split())

x = [0]*N
x[:] = map(int, input().split())

P = [0]*M
Y = [0]*M
for m in range(M):
    P[m], Y[m] = map(int, input().split())
    
all(nstr.count(c) for c in '753')
"""

N = int(input())
A, B = map(int, input().split())
P = [0]*N
P[:] = map(int, input().split())

P.sort()

num1 = len([i for i in P if i <= A])
num3 = len([i for i in P if i >= B+1])
num2 = N-num1-num3

num = min(num1, num2, num3)
print(num)