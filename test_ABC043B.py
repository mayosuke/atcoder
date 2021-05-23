# https://atcoder.jp/contests/abc042/tasks/abc043_b

def sol1(S):
    ans = []
    for s in S:
        if s == '0' or s == '1':
            ans.append(s)
        if ans and s == 'B':
            ans.pop()
    return ''.join(ans)

def sol(S):
    return sol1(S)

def test_1():
    assert sol('01B0') == '00'

def test_2():
    assert sol('0BB1') == '1'

# sol1(AC)
# S = input()
# ans = []
# for s in S:
# 	if s == '0' or s == '1':
# 		ans.append(s)
# 	if ans and s == 'B':
# 		ans.pop()
# print(''.join(ans))
