# https://atcoder.jp/contests/abc202/tasks/abc202_a

#  AC
def sol1(N): 
    return sum([7 - n for n in N])

def sol(N):
    return sol1(N)

def test_1():
    assert sol([1, 4, 3]) == 13

def test_2():
    assert sol([5, 6, 4]) == 6

# sol1
# N = [7 - int(n) for n in input().split()]
# print(sum(N))
