# https://atcoder.jp/contests/abc202/tasks/abc202_c

# TLE
def sol1(N,A,B,C):
    print()
    print(N, A, B, C)
    c = 0
    for i in range(N):
        print('i',i)
        for j in range(N):
            print('j',j)
            if A[i] == B[C[j]-1]:
                c += 1
    return c

# TLE
def sol2(N,A,B,C):
    import itertools
    c = 0
    for i, j in itertools.product(range(N), range(N)):
        if A[i] == B[C[j]-1]:
            c += 1
    return c

# AC
def sol3(N,A,B,C):
    print()
    count = {}
    for j in range(N):
        idx = B[C[j]-1]
        if idx in count:
            count[idx] += 1
        else:
            count[idx] = 1
    print(count)
    ans = 0
    for i in range(N):
        idx = A[i]
        if idx in count:
            ans += count[idx]
    return ans

# AC
def sol4(N,A,B,C):
    A = [n - 1 for n in A]
    B = [n - 1 for n in B]
    C = [n - 1 for n in C]
    count = [0] * N
    for j in range(N):
        count[B[C[j]]] += 1
    ans = 0
    for i in range(N):
        ans += count[A[i]]
    return ans

def sol(N,A,B,C):
    return sol4(N,A,B,C)

def test_1():
    assert sol(3,
        [1, 2, 2],
        [3, 1, 2],
        [2, 3, 2]
    ) == 4

def test_2():
    assert sol(4,
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 3, 4]
    ) == 16

def test_3():
    assert sol(3,
        [2, 3, 3],
        [1, 3, 3],
        [1, 1, 1]
    ) == 0

# sol1(TLE)
# N = int(input())
# A = [int(e) for e in input().split()]
# B = [int(e) for e in input().split()]
# C = [int(e) for e in input().split()]
# c = 0
# for i in range(N):
# 	for j in range(N):
# 		if A[i] == B[C[j] - 1]:
# 			c += 1
# print(c)

# sol2(TLE)
# import itertools
# N = int(input())
# A = [int(e) for e in input().split()]
# B = [int(e) for e in input().split()]
# C = [int(e) for e in input().split()]
# c = 0
# for i, j in itertools.product(range(N), range(N)):
# 	if A[i] == B[C[j] - 1]:
# 		c += 1
# print(c)

# sol3(AC) refered: https://atcoder.jp/contests/abc202/editorial/1859
# N = int(input())
# A = [int(e) for e in input().split()]
# B = [int(e) for e in input().split()]
# C = [int(e) for e in input().split()]
# count = {}
# for j in range(N):
# 	idx = B[C[j]-1]
# 	if idx in count:
# 		count[idx] += 1
# 	else:
# 		count[idx] = 1
# ans = 0
# for i in range(N):
# 	idx = A[i]
# 	if idx in count:
# 		ans += count[idx]
# print(ans)

# sol4(AC) refered: https://atcoder.jp/contests/abc202/submissions/22844172
# N = int(input())
# A = [int(e) - 1 for e in input().split()]
# B = [int(e) - 1for e in input().split()]
# C = [int(e) - 1for e in input().split()]
# count = [0] * N
# for j in range(N):
# 	count[B[C[j]]] += 1
# ans = 0
# for i in range(N):
# 	ans += count[A[i]]
# print(ans)
