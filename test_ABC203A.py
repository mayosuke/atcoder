# https://atcoder.jp/contests/abc203/tasks/abc203_a

def sol1(a,b,c):
    counts = {}
    for n in [a, b, c]:
        if not n in counts:
            counts[n] = 0
        counts[n] += 1
    l = len(counts)
    if l == 3:
        return 0
    elif l == 2:
        for k,v in counts.items():
            if v == 1:
                return k
    else:
        return a

def sol(a,b,c):
    return sol1(a,b,c)

def test_1():
    assert sol(2, 5, 2) == 5

def test_2():
    assert sol(4,5,6) == 0

def test_3():
    assert sol(1,1,1) == 1

# sol1(AC,12min)
# a,b,c = [int(i) for i in input().split()]
# counts = {}
# for n in [a, b, c]:
# 	if not n in counts:
# 		counts[n] = 0
# 	counts[n] += 1
# l = len(counts)
# if l == 3:
# 	print(0)
# elif l == 2:
# 	for k,v in counts.items():
# 		if v == 1:
# 			print(k)
# else:
# 	print(a)