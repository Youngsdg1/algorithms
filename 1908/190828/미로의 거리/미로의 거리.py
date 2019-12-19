import sys
sys.stdin = open("input.txt", "r")

def bfs(que):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    global visited
    global ans
    queue = [que]
    visited[que[0]][que[1]] = 1
    idxx = idyy = 0
    q = 1
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < n and 0 <= idx < n:
                if visited[idy][idx] == 0:
                    if arr[idy][idx] == 0 or arr[idy][idx] == 3:
                        queue.append([idy, idx])
                        visited[idy][idx] = visited[y][x] + 1
    if visited[end[0]][end[1]] == 0:
        return 0
    else:
        return visited[end[0]][end[1]] - 2

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[n-i-1][j] == 2:  # 밑에서 부터 찾는게 빠를것같아서
                start = [i, j]
            if arr[i][j] == 3:
                end = [n-i-1, j]
    visited = [[0] * n for _ in range(n)]
    ans = 0
    arr.reverse()
    print('#{} {}'.format(tc, bfs(start)))
