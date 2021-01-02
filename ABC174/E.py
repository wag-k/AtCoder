# -*- coding: utf-8 -*-


"""
#### 入力例 ####
N, X = map(int, input().split())
x = list(map(int, input().split()))
S = [input() for n in range(N)]
P = [0]*N
Y = [0]*N
for n in range(N):
    P[n], Y[n] = map(int, input().split())
"""


N, K = map(int, input().split())
A = list(map(int, input().split()))

def gauss(x):
    mod = x % 1
    res = x // 1
    if 0. < mod:
        res+=1
    #print("x: "+str(x)+ ", res: "+str(res))
    return res

def check(x, k):
    cnt = 0
    for a in A:
        cnt += gauss(a/x) - 1
        if k < cnt:
            return False
    return True

def bi(l, r):
    #print(l, r)
    if(r-l) <= 1:
        return print(r)
    mid = (l+r)//2
    if check(mid, K):
        bi(l, mid)
    else:
        bi(mid, r)

def main():
    A.sort(reverse=True)
    bi(0, A[0])
    return


if __name__ == '__main__':
    main()
