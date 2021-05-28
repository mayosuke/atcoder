# https://atcoder.jp/contests/abc046/tasks/abc046_a

def sol1(a,b,c):
    return len(set([a,b,c]))

def sol(a,b,c):
    return sol1(a,b,c)

def test_1():
    assert sol(3,1,4) == 3

def test_2():
    assert sol(3,3,33) == 2

# sol1(AC), 3min
# a, b, c = [int(i) for i in input().split()]
# print(len(set([a,b,c])))
