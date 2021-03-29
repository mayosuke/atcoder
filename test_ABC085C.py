# https://atcoder.jp/contests/abs/tasks/abc085_c

# TLE: 2283 ms	1979848 KB AC×6 TLE×17 MLE×1
def sol1(N, Y):
    print()
    print()
    # a: 10000yen, b: 5000yen, c: 1000yen
    # a + b + c = N
    from itertools import product
    candidates = list(product(*[[i for i in range(N+1)], [i for i in range(N+1)], [i for i in range(N+1)]]))
    print('candidates generated.')
    for c in candidates:
        if sum(c) == N and c[0] * 10000 + c[1] * 5000 + c[2] * 1000 == Y:
            return c
    return [-1, -1, -1]

# TLE: 2206 ms	9000 KB AC×13 TLE×11
def sol2(N, Y):
    print()
    print()
    # a: 10000yen, b: 5000yen, c: 1000yen
    # a + b + c = N
    print('candidates generated.')
    for a in range(N + 1): # 10000yen
        for b in range(N + 1): # 5000yen
            for c in range(N + 1): # 1000yen
                if sum([a, b, c]) == N and a * 10000 + b * 5000 + c * 1000 == Y:
                    return [a, b, c]
    return [-1, -1, -1]

# TLE: 2206 ms 9064 KB ACx13 TLE×11
def sol3(N, Y):
    print()
    print()
    # a: 10000yen, b: 5000yen, c: 1000yen
    # a + b + c = N
    print('candidates generated.')
    for a in range(N + 1): # 10000yen
        for b in range(N + 1 - a): # 5000yen
            for c in range(N + 1 - a - b): # 1000yen
                if a + b + c == N and a * 10000 + b * 5000 + c * 1000 == Y:
                    return [a, b, c]
    return [-1, -1, -1]

# AC 430 ms 9192 KB
def sol4(N, Y):
    print()
    print()
    # a: 10000yen, b: 5000yen, c: 1000yen
    # a + b + c = N
    print('candidates generated.')
    for a in range(N + 1): # 10000yen
        for b in range(N + 1 - a): # 5000yen
            c = N - a - b # 1000yen
            if a * 10000 + b * 5000 + c * 1000 == Y:
                return [a, b, c]
    return [-1, -1, -1]

def sol(N, Y):
    return sol4(N, Y)

def test_1():
    print(sol(9, 45000))

def test_2():
    print(sol(20, 196000))

def test_3():
    print(sol(1000, 1234000))


# passed solution:
# N, Y = [int(i) for i in input().split()]

# def sol4(N, Y):
#     for a in range(N + 1): # 10000yen
#         for b in range(N + 1 - a): # 5000yen
#             c = N - a - b # 1000yen
#             if a * 10000 + b * 5000 + c * 1000 == Y:
#                 return [a, b, c]
#     return [-1, -1, -1]

# ans = sol4(N, Y)
# print(ans[0], ans[1], ans[2])
