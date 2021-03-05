# 3
# 8 12 40
# 2

# 4
# 5 6 8 10
# 0

# 6
# 382253568 723152896 37802240 379425024 404894720 471526144
# 8

def all_even(arr):
    return len([n for n in arr if n % 2 != 0]) == 0

def answer(s):
    A = [int(n) for n in s.split()] # init state
    c = 0
    while all_even(A):
        A = [n / 2 for n in A]
        c += 1
    return c

def test_1():
    assert answer('8 12 40') == 2

def test_2():
    assert answer('5 6 8 10') == 0

def test_3():
    assert answer('382253568 723152896 37802240 379425024 404894720 471526144') == 8

