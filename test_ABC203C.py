# https://atcoder.jp/contests/abc203/tasks/abc203_c

def sol1(N,K,F):
    f = {}
    for i,k in F:
        if not i in f:
            f[i] = 0
        f[i] += k

    l = 0
    while K > 0:
        if l in f:
            K += f[l]
        K -= 1
        l += 1
    return l

def sol2(N,K,F):
    print()
    f = {}
    for i,k in F:
        if not i in f:
            f[i] = 0
        f[i] += k
    print(f)
    l = 0
    while True:
        if l in f:
            K += f[l]
        print(l,K)
        if K <= 0:
            break
        K -= 1
        l += 1
    return l

def sol3(N,K,F):
    # print()
    Fd = {}
    for i,k in F:
        if not i in Fd:
            Fd[i] = 0
        Fd[i] += k
    # print(Fd)
    Fp = [i for i in Fd.keys()]
    Fp.sort()
    # print(Fp)
    l = 0
    for fp in Fp:
        # print('l','K','fp')
        # print(l,K,fp)
        diff = fp - l
        # print('diff', diff)
        # print('K - diff', K - diff)
        if K - diff >= 0:
            l += diff
            K -= diff
            K += Fd[fp]
        else:
            break
    l = l + K
    # print(l)
    return l

def sol(N,K,F):
    return sol3(N,K,F)

def test_1():
    assert sol(2, 3,
        ((2, 1),
        (5, 10))
    ) == 4

def test_2():
    assert sol(5, 1000000000,
        ((1, 1000000000),
        (2, 1000000000),
        (3, 1000000000),
        (4, 1000000000),
        (5, 1000000000))
    ) == 6000000000

def test_3():
    assert sol(3, 2,
        ((5, 5),
        (2, 1),
        (2, 2))
    ) == 10

def test_4():
    assert sol(0, 2,
        ()
    ) == 2


# sol1 (WA)
# N,K = [int(i) for i in input().split()]
# F = [[int(j) for j in input().split()] for i in range(N)]
# f = {}
# for i,k in F:
# 	if not i in f:
# 		f[i] = 0
# 	f[i] += k
# l = 0
# while K > 0:
# 	if l in f:
# 		K += f[l]
# 	K -= 1
# 	l += 1
# print(l)

# sol2 (TLE)
# N,K = [int(i) for i in input().split()]
# F = [[int(j) for j in input().split()] for i in range(N)]
# f = {}
# for i,k in F:
# 	if not i in f:
# 		f[i] = 0
# 	f[i] += k
# l = 0
# while True:
# 	if l in f:
# 		K += f[l]
# 	if K <= 0:
# 		break
# 	K -= 1
# 	l += 1
# print(l)

# sol3 (AC,65min)
# N,K = [int(i) for i in input().split()]
# F = [[int(j) for j in input().split()] for i in range(N)]
# Fd = {}
# for i,k in F:
# 	if not i in Fd:
# 		Fd[i] = 0
# 	Fd[i] += k
# Fp = [i for i in Fd.keys()]
# Fp.sort()
# l = 0
# for fp in Fp:
# 	diff = fp - l
# 	if K - diff >= 0:
# 		l += diff
# 		K -= diff
# 		K += Fd[fp]
# 	else:
# 		break
# l = l + K
# print(l)
