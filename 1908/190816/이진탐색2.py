import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    book = []
    for i in range(p):
        book.append(i)
    # def binarySearch(book, low, high, key):
    low = 0
    high = len(book) - 1
    a_cnt = 0
    while low <= high:
        c = (low + high) // 2
        if book[c] == a:
            break
        elif book[c] > a:
            high = c - 1
            a_cnt += 1
        else:
            low = c + 1
            a_cnt += 1
    low = 0
    high = len(book) - 1
    b_cnt = 0
    while low <= high:
        c = (low + high) // 2
        if book[c] == b:
            break
        elif book[c] > b:
            high = c - 1
            b_cnt += 1
        else:
            low = c + 1
            b_cnt += 1

    if a_cnt < b_cnt:
        print('#{} {}'.format(tc, 'A'))
    elif b_cnt < a_cnt:
        print('#{} {}'.format(tc, 'B'))
    elif a_cnt == b_cnt:
        print('#{} {}'.format(tc, '0'))