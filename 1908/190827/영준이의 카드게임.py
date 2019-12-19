import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    card_alpha = []
    card_num = []
    real_card_num = []
    card = list(input())
    c = len(card)
    for i in range(0, c, 3):
        card_alpha.append(card[i])
    for j in range(1, c, 3):
        card_num.append(list(map(int, card[j:j+2])))
    for k in card_num:
        if k[0] == 0:
            real_card_num.append(k[1])
        elif k[0] == 1:
            real_card_num.append(k[0]*10+k[1])

    arr = [[0] * 14 for _ in range(4)]
    for i in range(len(card_alpha)):
        if card_alpha[i] == 'S':
            arr[0][real_card_num[i]] += 1
        elif card_alpha[i] == 'D':
            arr[1][real_card_num[i]] += 1
        elif card_alpha[i] == 'H':
            arr[2][real_card_num[i]] += 1
        elif card_alpha[i] == 'C':
            arr[3][real_card_num[i]] += 1
    cnt = 0
    for i in range(4):
        for j in range(14):
            if arr[i][j] >= 2:
                cnt += 1
                print('#{} ERROR'.format(tc))
                break
    if cnt == 0:
        s = 13 - sum(arr[0])
        d = 13 - sum(arr[1])
        h = 13 - sum(arr[2])
        c = 13 - sum(arr[3])
        print('#{} {} {} {} {}'.format(tc, s, d, h, c))