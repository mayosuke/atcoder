# https://atcoder.jp/contests/abc042/tasks/abc042_b

# AC
def sol1(S):
    S.sort()
    return ''.join(S)

def sol(S):
    return sol1(S)

def test_1():
    assert sol(['dxx', 'axx', 'cxx']) == 'axxcxxdxx'

# sol1
# N, L = [int(i) for i in input().split()]
# S = []
# for i in range(N):
# 	S.append(input())
# S.sort()
# print(''.join(S))
