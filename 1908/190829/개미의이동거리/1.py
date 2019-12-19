import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, list(input().split()))) for _ in range(n)]
    dx = [0, 0, -1, 1]  # 상 하
    dy = [-1, 1, 0, 0]  # 좌 우
    x = y = cnt = 0
    i = 1
    while 0 <= x < n and 0 <= y < n:
        cnt += 1
        if arr[x][y] != 0:
            if arr[x][y] == 1:
                if  i == 1:  # 좌 -> 우 : 상
                    i = 2
                elif i == 0:  # 우 -> 좌 : 하
                    i = 3
                elif i == 2:  # 하 -> 상 : 우
                    i = 1
                elif i == 3:  # 상 -> 하 : 좌
                    i = 0
            elif arr[x][y] == 2:
                if  i == 1:  # 좌 -> 우 : 하
                    i = 3
                elif i == 0:  # 우 -> 좌 : 상
                    i = 2
                elif i == 2:  # 하 -> 상 : 좌
                    i = 0
                elif i == 3:  # 상 -> 하 : 우
                    i = 1
            x += dx[i]
            y += dy[i]
        elif arr[x][y] == 0:
            x += dx[i]
            y += dy[i]

    print('#{} {}'.format(tc, cnt-1))
