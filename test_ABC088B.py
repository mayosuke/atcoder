# https://atcoder.jp/contests/abs/tasks/abc088_b


def sol1(N, A):
    ab = [0, 0]
    i = 0
    while A:
        print()
        print()
        print(N, A)
        v = max(A)
        A.remove(v)
        print(v)
        ab[i % 2] += v
        print(ab)
        i += 1
    return ab[0] - ab[1]

def sol2(N, A):
    ab = 0
    i = 0
    while A:
        print()
        print()
        print(N, A)
        v = max(A)
        A.remove(v)
        print(v)
        if i % 2 == 0:
            ab += v
        else:
            ab -= v
        print(ab)
        i += 1
    return ab

def sol(N, A):
    return sol2(N, A)

def test_1():
    assert sol(2, [3, 1]) == 2

def test_2():
    assert sol(3, [2, 7, 4]) == 5

def test_3():
    assert sol(4, [20, 18, 2, 18]) == 18


# passed solution:
# N = input()
# A = [int(a) for a in input().split()]

# def sol(N, A):
#     ab = 0
#     i = 0
#     while A:
#         v = max(A)
#         A.remove(v)
#         if i % 2 == 0:
#             ab += v
#         else:
#             ab -= v
#         i += 1
#     return ab

# print(sol(N, A))
