# https://atcoder.jp/contests/abs/tasks/arc089_a

def sol1(S):
    targets = 'dream dreamer erase eraser'.split()
    def func(s):
        print('s', s)
        for t in targets:
            print('t', t)
            if t == s:
                return True
            elif s.startswith(t):
                if func(s[len(t):]):
                    return True
        return False

    return 'YES' if func(S) else 'NO'



def sol(S):
    return sol1(S)

def test_1():
    assert sol('erasedream') == 'YES'

def test_2():
    assert sol('dreameraser') == 'YES'

def test_3():
    assert sol('dreamerer') == 'NO'



# solution:
