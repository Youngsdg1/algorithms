import sys
sys.stdin = open('input.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(x, y):
    global N, cnt
    cnt += 1
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            if arr[x][y] + 1 == arr[x + dx[i]][y + dy[i]]:
                dfs(x + dx[i], y + dy[i])

T = int(input())
for tc in range(1, 1 + T):
    print('#%d' % (tc), end=' ')
    N = int(input())
    max_cnt = 0
    idd = []
    arr = [list(map(int, input().split())) for _ in range(N)]
    for a in range(N):
        for b in range(N):
            cnt = -1
            dfs(a, b)
            if cnt >= max_cnt:
                idd.append([arr[a][b], cnt])
                max_cnt = cnt
    min_v = 1000000
    for ide in range(len(idd)):
        if idd[ide][1] == max_cnt:
            if min_v > idd[ide][0]:
                min_v = idd[ide][0]
    print(min_v, max_cnt + 1)