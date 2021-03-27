# https://atcoder.jp/contests/abs/tasks/abc087_b

# A: 500yen, B: 100yen, C: 50yen
def calc(a, b, c):
    return 500 * a + 100 * b + 50 * c

def sol(A, B, C, X):
    print()
    print()
    print(f'input: A={A}, B={B}, C={C}, X={X}')

    # search words: python combinations of multiple lists
    # python - All combinations of a list of lists - Stack Overflow
    # https://stackoverflow.com/questions/798854/all-combinations-of-a-list-of-lists
    from itertools import product
    candidates = list(product(*[[a for a in range(A+1)], [b for b in range(B+1)], [c for c in range(C+1)]]))
    # print('candidates', candidates)
    
    ans = [(a, b, c) for a, b, c in candidates if calc(a, b, c) == X]
    print(ans)

    return len(ans)

def test_1():
    assert sol(2, 2, 2, 100) == 2

def test_2():
    assert sol(5, 1, 0, 150) == 0

def test_3():
    assert sol(30, 40, 50, 6000) == 213

# passed solution:
# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

# def calc(a, b, c):
#     return 500 * a + 100 * b + 50 * c

# from itertools import product
# candidates = list(product(*[[a for a in range(A+1)], [b for b in range(B+1)], [c for c in range(C+1)]]))    
# ans = [(a, b, c) for a, b, c in candidates if calc(a, b, c) == X]
# print(len(ans))
