# https://atcoder.jp/contests/abc043/tasks/abc043_a

def sol1(N):
    return sum(range(1, N + 1))

def sol(N):
    return sol1(N)

def test_1():
    assert sol(3) == 6

def test_2():
    assert sol(10) == 55

def test_3():
    assert sol(1) == 1


# sol1(AC)
# N = int(input())
# print(sum(range(1, N + 1)))
