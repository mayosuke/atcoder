# https://atcoder.jp/contests/abc045/tasks/abc045_b

# AC
def sol1(sa,sb,sc):
    print()
    cards = {
        'a': list(sa),
        'b': list(sb),
        'c': list(sc)
    }
    turn = 'a'
    while True:
        print(turn, cards)
        if not cards[turn]:
            break
        turn = cards[turn].pop(0)
    return turn.upper()

def sol2(sa,sb,sc):
    print()
    cards = {
        'a': list(sa),
        'b': list(sb),
        'c': list(sc)
    }
    turn = 'a'
    while cards[turn]:
        print(turn, cards)
        turn = cards[turn].pop(0)
    return turn.upper()

def sol(sa,sb,sc):
    return sol2(sa,sb,sc)

def test_1():
    assert sol(
        'aca',
        'accc',
        'ca'
    ) == 'A'

def test_2():
    assert sol(
        'abcb',
        'aacb',
        'bccc',
    ) == 'C'

# sol1
# cards = {
# 	'a': list(input()),
# 	'b': list(input()),
# 	'c': list(input())
# }
# turn = 'a'
# while True:
# 	if not cards[turn]:
# 		break
# 	turn = cards[turn].pop(0)
# print(turn.upper())

# sol2
# cards = {
# 	'a': list(input()),
# 	'b': list(input()),
# 	'c': list(input())
# }
# turn = 'a'
# while cards[turn]:
# 	turn = cards[turn].pop(0)
# print(turn.upper())
