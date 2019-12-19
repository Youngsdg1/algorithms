import sys
sys.stdin = open('tnt.txt','r')
def merge_check(left, right, card):
    if card[left] == card[right]:
        return left
    if card[left] == 1:
        if card[right] == 2:
            return right
        else:
            return left
    elif card[left] == 2:
        if card[right] == 3:
            return right
        else:
            return left
    else:
        if card[right] == 1:
            return right
        else:
            return left

def Binary_Search(start, end, card):
    if start == end:
        return start
    left = Binary_Search(start, (start+end)//2, card)
    right = Binary_Search((start+end)//2+1, end, card)
    return merge_check(left, right, card)
for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, Binary_Search(0, N-1, cards)+1))