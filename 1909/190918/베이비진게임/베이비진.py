import sys
sys.stdin = open('input.txt', 'r')
def runn(list):
    for i in range(8):
        if list[i] >= 1 and list[i+1] >= 1 and list[i+2] >= 1:
            return True
def who():
    card1 = [0 for i in range(10)]
    card2 = [0 for i in range(10)]
    for i in range(12):
        if i % 2 == 0:
            card1[num_list[i]] += 1
        else:
            card2[num_list[i]] += 1
        if card1[num_list[i]] == 3:
            return 1
        if runn(card1):
            return 1
        if card2[num_list[i]] == 3:
            return 2
        if runn(card2):
            return 2
        if i == len(num_list)-1:
            return 0
for tc in range(1, int(input())+1):
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(tc, who()))