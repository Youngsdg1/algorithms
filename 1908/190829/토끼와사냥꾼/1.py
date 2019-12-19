import sys
sys.stdin = open('input.txt', 'r')
arr = [list(map(int, input().split())) for _ in range(10)]

def find_rabbit(x, y, i):
    # d = [ 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    cnt = 0
    while 0 <= x+dx[i] < 10 and 0 <= y+dy[i] < 10:  # 한 방향으로 쭉 찾는거.
        x += dx[i]
        y += dy[i]
        if arr[x][y] == 1:
            cnt += 1
            arr[x][y] = 5
        elif arr[x][y] == 2:
            break
        elif arr[x][y] == 0:
            pass
    return cnt

result = 0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 3:
            for k in range(8):
                result += (find_rabbit(i, j, k))
print(result)


