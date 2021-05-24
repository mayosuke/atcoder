# https://atcoder.jp/contests/abc044/tasks/abc044_a

# AC
def sol1(N,K,X,Y):
    return N * X if N <= K else K * X + (N - K) * Y

def sol(N,K,X,Y):
    return sol1(N,K,X,Y)

def test_1():
    assert sol(5, 3, 10000, 9000) == 48000

def test_2():
    assert sol(2, 3, 10000, 9000) == 20000

# sol1
# N = int(input())
# K = int(input())
# X = int(input())
# Y = int(input())
# print(N * X if N <= K else K * X + (N - K) * Y)
