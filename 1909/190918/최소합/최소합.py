import sys
sys.stdin = open('input.txt', 'r')
# 최소한의 길이로 가게끔.
def dfs(x, y, s):
    global minsum, n
    if x == n - 1 and y == n - 1:  # 도착지점
        if minsum > s:
            minsum = s
    if minsum < s:  # 목적지 도착 전에 큰 값이 있으면 가지치기
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and  0 <= ny < n:
            s += arr[nx][ny]
            dfs(nx, ny, s)
            s -= arr[nx][ny]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s = arr[0][0]
    dx = [1, 0]
    dy = [0, 1]
    minsum = 100000
    dfs(0, 0, s)
    print('#{} {}'.format(tc, minsum))