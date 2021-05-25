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

def sol(w):
    return sol1(w)

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
