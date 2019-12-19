import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
dx = [0, 0, -1, 1]  # 상 하
dy = [-1, 1, 0, 0]  # 좌 우
cnt = 0
def giji_1(arr, x, y):
    global cnt
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:
            x += dx[i]
            y += dy[i]
            if arr[x][y] == 'H':
                cnt += 1
                arr[x][y] == 'X'
    return cnt
def giji_2(arr, x, y):
    global cnt
    for _ in range(2):
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                x += dx[i]
                y += dy[i]
                if arr[x][y] == 'H':
                    cnt += 1
                    arr[x][y] == 'X'
        x += dx[i]
        y += dy[i]
    return cnt
def giji_3(arr, x, y):
    global cnt
    for _ in range(3):
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                x += dx[i]
                y += dy[i]
                if arr[x][y] == 'H':
                    cnt += 1
                    arr[x][y] == 'X'
        x += dx[i]
        y += dy[i]
    return cnt
result = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] == 'A':
            result += giji_1(arr, i, j)
print(sum(arr, []).count('H')-result)