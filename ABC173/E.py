# -*- coding: utf-8 -*-

import collections
import math
import heapq
import sys


def solve(n, k, aaa):
    pos = []
    neg = []
    MOD = 10 ** 9 + 7
    for a in aaa:
        if a > 0:
            pos.append(a)
        elif a < 0:
            neg.append(a)
    if len(pos) + len(neg) < k:
        return 0
    if len(pos) == 0:
        if k % 2 == 1:
            if len(neg) < n:
                return 0
            neg.sort(reverse=True)
        else:
            neg.sort()
        ans = 1
        for a in neg[:k]:
            ans = ans * a % MOD
        return ans
    if len(pos) + len(neg) == k:
        if n > k and len(neg) % 2 == 1:
            return 0
        ans = 1
        for a in pos:
            ans = ans * a % MOD
        for a in neg:
            ans = ans * a % MOD
        return ans

    pos.sort()
    neg.sort(reverse=True)

    ans = 1
    r = k
    while r >= 2:
        if len(pos) <= 1:
            ans = ans * neg.pop() * neg.pop() % MOD
        elif len(neg) <= 1:
            ans = ans * pos.pop() * pos.pop() % MOD
        else:
            pm = pos[-1] * pos[-2]
            nm = neg[-1] * neg[-2]
            if pm > nm:
                ans = ans * pm % MOD
                pos.pop()
                pos.pop()
            else:
                ans = ans * nm % MOD
                neg.pop()
                neg.pop()
        r -= 2

    if r == 1:
        ans = ans * pos[-1] % MOD

    return ans


n, k, *aaa = map(int, sys.stdin.buffer.read().split())
print(solve(n, k, aaa))

"""
#### 入力例 ####
N, X = map(int, input().split())

x = list(map(int, input().split()))

P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
"""
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 +7

def main():
    ans = 1
    A.sort(reverse=True)
    if N == K:
        for n in range(N):
            ans*=A[n]
        print(ans % mod)
        return
    
    M = collections.deque()
    P = collections.deque()
    for n in range(N):
        if A[n] < 0:
            M.append(A[n])
        elif 0 < A[n]:
            P.append(A[n])
    if len(P) + len(M) < K:
        print(0)
        return
    if len(P) == 0:
        if(K%2 == 1):
            if (len(M)< N):
                print(0)
                return
            for k in range(K):
                ans = ans * M.popleft() % mod
            print(ans)
            return
        else:
            for k in range(K):
                ans = ans * M.pop() % mod
            print(ans)
            return
    if len(P) + len(M) == K:
        if K < N and len(M) % 2 == 1:
            print(0)
            return
        ans = 1
        while not len(P) == 0:
            ans = ans * P.popleft() % mod
        while not len(M) == 0:
            ans = ans * M.pop() % mod
        print(ans)
        return 
    k = 0
    while k <= K-2:
        if len(P) < 2:
            ans *= M.pop() * M.pop() % mod
        elif len(M) <2:
            ans *= P.pop() * P.pop() % mod
        else:
            if (P[0]*P[1] <= M[-1]*M[-2]):
                ans *= M.pop() * M.popleft() % mod
            else:
                ans *= P.pop() * P.pop() % mod
        k+=2
    if k == K-1:
        ans *= P.pop() % mod

    print(ans)
    return

if __name__ == '__main__':
    main()
"""