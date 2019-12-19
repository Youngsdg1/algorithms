import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())

    low = 0
    high = p
    a_cnt = 0
    while low <= high:
        c = (low + high) // 2
        if c == a:
            break
        elif c > a:
            high = c
            a_cnt += 1
        else:
            low = c
            a_cnt += 1
    low = 0
    high = p
    b_cnt = 0
    while low <= high:
        c = (low + high) // 2
        if c == b:
            break
        elif c > b:
            high = c
            b_cnt += 1
        else:
            low = c
            b_cnt += 1

    if a_cnt < b_cnt:
        print('#{} {}'.format(tc, 'A'))
    elif b_cnt < a_cnt:
        print('#{} {}'.format(tc, 'B'))
    elif a_cnt == b_cnt:
        print('#{} {}'.format(tc, '0'))