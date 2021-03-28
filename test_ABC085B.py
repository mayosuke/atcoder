# https://atcoder.jp/contests/abs/tasks/abc085_b


def sol1(D):
    print()
    print()
    km = []
    while D:
        print(km)
        print(D)
        m = max(D)
        while m in D:
            D.remove(m)
        km.append(m)
    print(km)
    return len(km)

def sol(D):
    return sol1(D)

def test_1():
    assert sol([10, 8, 8, 6]) == 3

def test_2():
    assert sol([15, 15, 15]) == 1

def test_3():
    assert sol([50, 30, 50, 100, 50, 80, 30]) == 4


# passed solution:
# N = int(input())
# D = [int(input()) for i in range(N)]

# def sol1(D):
#     km = []
#     while D:
#         m = max(D)
#         while m in D:
#             D.remove(m)
#         km.append(m)
#     return len(km)

# print(sol1(D))
