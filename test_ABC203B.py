# https://atcoder.jp/contests/abc203/tasks/abc203_b

def sol1(N,K):
    t = 0
    for n in range(1, N+1):
        for k in range(1, K+1):
            t += n*100 + k
    return t

def sol(N,K):
    return sol1(N,K)

def test_1():
    assert sol(1, 2) == 203

def test_2():
    assert sol(3, 3) == 1818


# sol1(AC,8min)
# N, K = [int(i) for i in input().split()]
# t = 0
# for n in range(1, N+1):
# 	for k in range(1, K+1):
# 		t += n*100 + k
# print(t)
