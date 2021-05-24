# https://atcoder.jp/contests/abc045/tasks/abc045_a

# AC
def sol1(a,b,h):
    return int((a + b) * h / 2)

def sol(a,b,h):
    return sol1(a,b,h)

def test_1():
    assert sol(3,4,2) == 7

def test_2():
    assert sol(4,4,4) == 16

# sol1
# a = int(input())
# b = int(input())
# h = int(input())
# print(int((a + b) * h / 2))
