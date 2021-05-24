# https://atcoder.jp/contests/abc051/tasks/abc051_c

# AC
def sol1(sx, sy, tx, ty):
    ans = []
    # 1
    for y in range(sy, ty):
        ans.append('U')
    for x in range(sx, tx):
        ans.append('R')
    # 2
    for y in range(ty, sy, -1):
        ans.append('D')
    for x in range(tx, sx, -1):
        ans.append('L')
    # 3
    ans.append('L')
    for y in range(sy, ty + 1):
        ans.append('U')
    for x in range(sx, tx + 1):
        ans.append('R')
    ans.append('D')
    # 4
    ans.append('R')
    for y in range(ty, sy - 1, -1):
        ans.append('D')
    for x in range(tx, sx - 1, -1):
        ans.append('L')
    ans.append('U')
    return ''.join(ans)

def sol(sx,sy,tx,ty):
    return sol1(sx,sy,tx,ty)

def test_1():
    assert sol(0, 0, 1, 2) == 'UURDDLLUUURRDRDDDLLU'

def test_2():
    assert sol(-2, -2, 1, 1) == 'UURRURRDDDLLDLLULUUURRURRDDDLLDL' # UUURRRDDDLLLLUUUURRRRDRDDDDLLLLU

# sol1
# sx, sy, tx, ty = [int(i) for i in input().split()]
# ans = []
# # 1
# for y in range(sy, ty):
# 	ans.append('U')
# for x in range(sx, tx):
# 	ans.append('R')
# # 2
# for y in range(ty, sy, -1):
# 	ans.append('D')
# for x in range(tx, sx, -1):
# 	ans.append('L')
# # 3
# ans.append('L')
# for y in range(sy, ty + 1):
# 	ans.append('U')
# for x in range(sx, tx + 1):
# 	ans.append('R')
# ans.append('D')
# # 4
# ans.append('R')
# for y in range(ty, sy - 1, -1):
# 	ans.append('D')
# for x in range(tx, sx - 1, -1):
# 	ans.append('L')
# ans.append('U')
# print(''.join(ans))
