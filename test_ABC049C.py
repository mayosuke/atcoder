# https://atcoder.jp/contests/abs/tasks/arc065_a

# AC × 3 WA × 16
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


# ACx11 WAx8
def sol2(S: str):
    print()
    print()
    print(S)
    targets = 'dreameraser dreamer dream eraser erase'.split()
    i = 0
    while True:
        print(i)
        prev_i = i
        for t in targets:
            if S[i:].startswith(t):
                print(t, S[i:])
                i += len(t)
        if i == len(S):
            return 'YES'
        elif i == prev_i:
            return 'NO'


# ACx11 WAx8
def sol3(S: str):
    print()
    print()
    print(S)
    targets = 'dreamerasedreamer dreameraser dreamer dream eraser erase'.split()
    i = 0
    while True:
        print(i)
        prev_i = i
        for t in targets:
            if S[i:].startswith(t):
                print(t, S[i:])
                i += len(t)
                break
        if i == len(S):
            return 'YES'
        elif i == prev_i:
            return 'NO'

# ACx11 WAx8
def sol4(S: str):
    print()
    print()
    print(len(S), S)
    targets = 'dreamerasedreamer dreameraser dreamerase dreamer dream eraser erase'.split()
    i = 0
    while True:
        print(i)
        prev_i = i
        for t in targets:
            if S[i:].startswith(t):
                print(t, S[i:])
                i += len(t)
                break
        if i == len(S):
            return 'YES'
        elif i == prev_i:
            return 'NO'

# AC
def sol5(S: str):
    print()
    print()
    print(len(S), S)
    targets = 'dreameraser dreamerase dreamer dream eraser erase'.split()
    i = 0
    while True:
        print(i)
        prev_i = i
        for t in targets:
            if S[i:].startswith(t):
                print(t, S[i:])
                i += len(t)
                break
        if i == len(S):
            return 'YES'
        elif i == prev_i:
            return 'NO'


def sol(S):
    return sol5(S)

def test_1():
    assert sol('erasedream') == 'YES'

def test_2():
    assert sol('dreameraser') == 'YES'

def test_3():
    assert sol('dreamerer') == 'NO'

def test_4():
    assert sol('dreamxerer') == 'NO'

def test_6():
    assert sol('dreameraserdream') == 'YES'

def test_7():
    assert sol('dreamrase') == 'NO'

def test_8():
    assert sol('d') == 'NO'

def test_9():
    assert sol('dr') == 'NO'

def test_10():
    assert sol('dre') == 'NO'

def test_11():
    assert sol('drea') == 'NO'

def test_12():
    assert sol('dream') == 'YES'

def test_13():
    assert sol('dream'*(int(100000/len('dream')))) == 'YES'

def test_14():
    assert sol('dream'*19999 + 'xxxxx') == 'NO'

def test_15():
    assert sol('dreamerasedreamer') == 'YES'

def test_16():
    assert sol('dreameraserdreamer') == 'YES'

def test_17():
    assert sol('dreameraseerase') == 'YES'

def test_18():
    assert sol('dreamedream') == 'NO'

def test_18a():
    assert sol('dreamdream') == 'YES'

def test_19():
    assert sol('dreamedreamer') == 'NO'

def test_19a():
    assert sol('dreamdreamer') == 'YES'

def test_20():
    assert sol('dreamerdreamer') == 'YES'

def test_21():
    assert sol('dreamerdream') == 'YES'

def test_22():
    assert sol('dreamererase') == 'YES'

def test_23():
    assert sol('dreamereraser') == 'YES'

def test_24():
    assert sol('erasererase') == 'YES'

def test_25():
    assert sol('erasereraser') == 'YES'

def test_26():
    assert sol('eraseerase') == 'YES'

def test_27():
    import itertools
    t = ['dreamer', 'dream', 'eraser', 'erase']
    for e in set([p[0]+p[1]+p[2] for p in itertools.product(t, t, t)]):
        assert sol(e) == 'YES'

def test_28():
    import itertools
    t = ['dreamer', 'dream', 'eraser', 'erase', 'x']
    for e in set([p[0]+p[1]+p[2]+p[3] for p in itertools.product(t, t, t, t)]):
        if 'x' in e:
            assert sol(e) == 'NO'
        else:
            assert sol(e) == 'YES'

def test_29():
    assert sol('dreamerasedreamerase') == 'YES'

# solution:
# S = input()

# targets = 'dreameraser dreamerase dreamer dream eraser erase'.split()
# def sol2(S):
# 	i = 0
# 	while True:
# 		prev_i = i
# 		for t in targets:
# 			if S[i:].startswith(t):
# 				i += len(t)
# 				break
# 		if i == len(S):
# 			return 'YES'
# 		elif i == prev_i:
# 			return 'NO'

# print(sol2(S))
