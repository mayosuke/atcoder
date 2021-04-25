# https://atcoder.jp/contests/arc117/tasks/arc117_b

def sol1(A, B):
    print()
    print('A', A)
    print('B', B)
    C = A * B
    print('C', C)
    EA = [i for i in range(1, A + 1)]
    print('EA', EA)
    EB = [i for i in range(1, B + 1)]
    print('EB', EB)

    diff = abs(sum(EA) - sum(EB))
    print('diff', diff)
    if A > B:
        EB[-1] = EB[-1] + diff
    elif A < B:
        EA[-1] = EA[-1] + diff
    print('EA', EA)
    print('EB', EB)

    ans =  EA + [-i for i in EB]
    print(ans)
    return ans

def sol(A, B):
    return sol1(A, B)

def test_1():
    assert sol([1, 2]) == 4

def test_2():
    assert sol(5, 3, 4, 1, 5, 2) == 32

def test_3():
    assert sol([314, 159, 265, 358, 979, 323, 846]) == 492018656


# solution:
