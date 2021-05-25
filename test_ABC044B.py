# https://atcoder.jp/contests/abc044/tasks/abc044_b

# AC
def sol1(w):
    from collections import Counter
    count = Counter(w)
    print()
    print(count)
    for c in count.values():
        if c % 2:
            return 'No'
    return 'Yes'

# AC (refered: https://atcoder.jp/contests/abc044/submissions/22731036)
def sol2(w):
    for c in w:
        if w.count(c) % 2:
            return 'No'
    return 'Yes'

def sol(w):
    return sol2(w)

def test_1():
    assert sol('abaccaba') == 'Yes'

def test_2():
    assert sol('hthth') == 'No'

# sol1
# from collections import Counter
# w = input()
# count = Counter(w)
# for c in count.values():
# 	if c % 2:
# 		print('No')
# 		break
# else:
# 	print('Yes')

# sol2
# w = input()
# for c in w:
# 	if w.count(c) % 2:
# 		print('No')
# 		break
# else:
# 	print('Yes')
