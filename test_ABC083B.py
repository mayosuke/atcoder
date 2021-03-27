# https://atcoder.jp/contests/abs/tasks/abc083_b

def sum_of_each_digit(N):
    return sum([int(d) for d in str(N)])

def sol(N, A, B):
    ans = 0
    for n in range(1, N+1):
        soed = sum_of_each_digit(n)
        if soed >= A and soed <= B:
            ans += n
    return ans

def test_1():
    assert sol(20, 2, 5) == 84

def test_2():
    assert sol(10, 1, 2) == 13

def test_3():
    assert sol(100, 4, 16) == 4554


# passed solution:
# N, A, B = [int(s) for s in input().split()]

# def sum_of_each_digit(N):
#   return sum([int(d) for d in str(N)])

# def sol(N, A, B):
#   ans = 0
#   for n in range(1, N+1):
#     soed = sum_of_each_digit(n)
#     if soed >= A and soed <= B:
#       ans += n
#   return ans

# print(sol(N, A, B))
