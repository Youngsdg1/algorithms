def check(a, b, card):
    if card[a] == card[b]:
        return a
    if card[a] is 1:
        if card[b] is 2:
            return b
        else:
            return a
    elif card[a] == 2:
        if card[b] is 3:
            return b
        else:
            return a
    else:
        if card[b] == 1:
            return b
        else:
            return a
def rec(st, ed, card):
    if st == ed:
        return st
    l = rec(st, (st + ed)//2, card)
    r = rec((st + ed)//2 + 1, ed, card)
    return check(l, r, card)
import sys
sys.stdin = open('tnt.txt','r')
def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        card = list(map(int, input().split()))
        print("#{} {}".format(tc, rec(0, N-1, card) + 1))
main()