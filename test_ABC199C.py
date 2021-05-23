# https://atcoder.jp/contests/abc199/tasks/abc199_c

# TLE
def sol1(N, S, TQ): 
    print()

    for tq in TQ:
        T, A, B = [i for i in tq]
        if T == 1:
            if B < A:
                A, B = B, A
            S = ''.join(S[:A-1]) + S[B-1] + ''.join(S[A:B-1]) + S[A-1] + ''.join(S[B:])
        else:
            S = S[N:] + S[:N]

    return S

# TLE
def sol2(N, S, TQ): 
    print()
    S = [c for c in S]
    for tq in TQ:
        T, A, B = [i for i in tq]
        if T == 1:
            if B < A:
                A, B = B, A
            S = S[:A-1] + [S[B-1]] + S[A:B-1] + [S[A-1]] + S[B:]
        else:
            S = S[N:] + S[:N]

    return ''.join(S)

# TLE
def sol3(N, S, TQ): 
    print()
    S = [c for c in S]
    for tq in TQ:
        T, A, B = [i for i in tq]
        if T == 1:
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            S = S[N:] + S[:N]

    return ''.join(S)

# TLE
def sol4(N, S, TQ): 
    print()
    S = [c for c in S]
    for tq in TQ:
        T, A, B = [i for i in tq]
        if T == 1:
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            for i in range(N):
                S[i+N], S[i] = S[i], S[i+N]

    return ''.join(S)

# AC (Referred: https://atcoder.jp/contests/abc199/editorial/1162)
def sol5(N, S, TQ): 
    print()
    S = [c for c in S]
    flipped = False
    for tq in TQ:
        T, A, B = [i for i in tq]
        if T == 1:
            if flipped:
                A = A + N if A <= N else A - N
                B = B + N if B <= N else B - N
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            flipped = not flipped
    if flipped:
        S = S[N:] + S[:N]
    return ''.join(S)

def sol(N, S, T):
    return sol5(N, S, T)

def test_1():
    assert sol(2, 'FLIP', [
        [2,0,0],
        [1,1,4]
    ]) == 'LPFI'

def test_2():
    assert sol(2, 'FLIP',[
        [1, 1, 3],
        [2, 0, 0],
        [1, 1, 2],
        [1, 2, 3],
        [2, 0, 0],
        [1, 1, 4]
    ]) == 'ILPF'


# sol1(TLE)
# N = int(input())
# S = input()
# Q = int(input())
# for i in range(Q):
# 	T, A, B = [int(i) for i in input().split()]
# 	if T == 1:
# 		if B < A:
# 			A, B = B, A
# 		S = ''.join(S[:A-1]) + S[B-1] + ''.join(S[A:B-1]) + S[A-1] + ''.join(S[B:])
# 	else:
# 		S = S[N:] + S[:N]
# print(S)

# sol2(TLE)
# N = int(input())
# S = [c for c in input()]
# Q = int(input())
# for i in range(Q):
# 	T, A, B = [int(i) for i in input().split()]
# 	if T == 1:
# 		if B < A:
# 			A, B = B, A
# 		S = S[:A-1] + [S[B-1]] + S[A:B-1] + [S[A-1]] + S[B:]
# 	else:
# 		S = S[N:] + S[:N]
# print(''.join(S))

# sol3(TLE)
# N = int(input())
# S = [c for c in input()]
# Q = int(input())
# for i in range(Q):
# 	T, A, B = [int(i) for i in input().split()]
# 	if T == 1:
# 		S[A-1], S[B-1] = S[B-1], S[A-1]
# 	else:
# 		S = S[N:] + S[:N]
# print(''.join(S))

# sol4(TLE)
# N = int(input())
# S = [c for c in input()]
# Q = int(input())
# for i in range(Q):
# 	T, A, B = [int(i) for i in input().split()]
# 	if T == 1:
# 		S[A-1], S[B-1] = S[B-1], S[A-1]
# 	else:
# 		for i in range(N):
# 			S[i+N], S[i] = S[i], S[i+N]
# print(''.join(S))

# sol5 (AC, Referred: https://atcoder.jp/contests/abc199/editorial/1162)
# N = int(input())
# S = [c for c in input()]
# Q = int(input())
# flipped = False
# for i in range(Q):
# 	T, A, B = [int(i) for i in input().split()]
# 	if T == 1:
# 		if flipped:
# 			A = A + N if A <= N else A - N
# 			B = B + N if B <= N else B - N
# 		S[A-1], S[B-1] = S[B-1], S[A-1]
# 	else:
# 		flipped = not flipped
# if flipped:
# 	S = S[N:] + S[:N]
# print(''.join(S))
