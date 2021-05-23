# https://atcoder.jp/contests/abc199/tasks/abc199_b

def sol1(A, B):
    print()
    print('A', A)
    print('B', B)

    ans = None
    print('ans', ans)
    for a, b in zip(A, B):
        c = set(range(a, b + 1))
        print('a', 'b', 'c', a, b, c)
        ans = c if ans is None else ans & c
        print('ans', ans)

    return len(ans)

def sol2(A, B):
    print()
    print('A', A)
    print('B', B)

    a = max(A)
    b = min(B)
    ans = [i for i in range(a, b+1)]
    print(ans)
    return len(ans)

def sol(A, B):
    return sol2(A, B)

def test_1():
    assert sol([3, 2], [7, 5]) == 3

def test_2():
    assert sol([1, 5, 3], [10, 7, 3]) == 0  

def test_3():
    assert sol([3, 2, 5], [6, 9, 8]) == 2

def test_4():
    assert sol([1, 2, 3], [1, 2, 3]) == 0


# sol1 (WA)
# N = input()
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# ans = None
# for a, b in zip(A, B):
#   c = set(range(a, b + 1))
#   ans = ans & c if ans else c
# print(len(ans))

# sol2 (AC)
# N = input()
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# ans = None
# for a, b in zip(A, B):
#   c = set(range(a, b + 1))
#   ans = c if ans is None else ans & c
# print(len(ans))

# sol3 (AC, refered: https://atcoder.jp/contests/abc199/editorial/1161)
# N = input()
# A = max([int(i) for i in input().split()])
# B = min([int(i) for i in input().split()])
# ans = [i for i in range(A, B+1)]
# print(len(ans))
