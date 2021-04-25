# https://atcoder.jp/contests/abc199/tasks/abc199_a

def sol1(A, B, C):
    print()
    print('A', A)
    print('B', B)
    print('C', C)
    return 'Yes' if A**2 + B**2 < C**2 else 'No'

def sol(A, B, C):
    return sol1(A, B, C)

def test_1():
    assert sol(2, 2, 4) == 'Yes'

def test_2():
    assert sol(10, 10, 10) == 'No'

def test_3():
    assert sol(3, 4, 5) == 'No'


# solution:
