# https://atcoder.jp/contests/abc042/tasks/abc042_a

# WA
def sol1(A):
    if A.count(5) == 2 and A.count(7) == 1:
        return 'YES'
    return 'NO'

def sol(A):
    return sol1(A)

def test_yes_1():
    assert sol([5, 5, 7]) == 'YES'

def test_yes_2():
    assert sol([7, 5, 5]) == 'YES'

def test_yes_3():
    assert sol([5, 7, 5]) == 'YES'

def test_all():
    from itertools import product
    for i in product(range(1, 11), range(1,11),range(1,11)):
        i = list(i)
        if i == [5, 5, 7] or i == [5, 7, 5] or i == [7, 5, 5]:
            assert sol(i) == 'YES'
        else:
            assert sol(i) == 'NO'

def test_no_1():
    assert sol([7, 7, 5]) == 'NO'

def test_no_2():
    assert sol([7, 7, 7]) == 'NO'

def test_no_3():
    assert sol([1, 1, 1]) == 'NO'

def test_no_4():
    assert sol([10, 10, 10]) == 'NO'


# AC refered: https://atcoder.jp/contests/abc042/submissions/22842105
# A = input()
# if A.count('5') == 2 and A.count('7') == 1:
# 	print('YES')
# else:
# 	print('NO')
