import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(CP):
    global virus_cnt, time_cnt, M
    visited = [[0] * N for _ in range(N)]
    n = 1
    visited[CP[0]][CP[1]] = 'activate'
    queue = [CP]
    while queue:
        time_cnt += 1
        n += 1
        for _ in range(len(queue)):
            a = queue.pop(0)
            x = a[0]
            y = a[1]
            for i in range(4):
                idx = x + dx[i]
                idy = y + dy[i]
                if 0 <= idx < N and 0 <= idy < N:
                    if visited[idx][idy] == 0:
                        if arr[idx][idy] == 0:
                            queue.append([idx, idy])
                            visited[idx][idy] = n
                        elif arr[idx][idy] == 2:
                            virus_cnt += 1
                            queue.append([idx, idy])
                            visited[idx][idy] = 'activate'
                            if virus_cnt == M:
                                return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_value = 999999999999999999999
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_cnt = 1
            time_cnt = 0
            bfs([i, j])
            if time_cnt < min_value:
                min_value = time_cnt
print(min_value)