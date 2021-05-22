# https://atcoder.jp/contests/abc202/tasks/abc202_b

# AC
def sol1(S):
    S = list(S)
    S.reverse()
    for i, s in enumerate(S):
        if s == '6':
            S[i] = '9'
        elif s == '9':
            S[i] = '6'
    return ''.join(S)

def sol(S):
    return sol1(S)

def test_1():
    assert sol('0601889') == '6881090'

def test_2():
    assert sol('86910') == '01698'

def test_3():
    assert sol('01010') == '01010'

# sol1
# S = list(input())
# S.reverse()
# for i, s in enumerate(S):
# 	if s == '6':
# 		S[i] = '9'
# 	elif s == '9':
# 		S[i] = '6'
# print(''.join(S))
