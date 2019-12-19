import sys
sys.stdin = open('input.txt', 'r')

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    visited = [[0] * N for _ in range(N)]
    united = [[x, y]]
    sum = 0
    while queue:
        for i in range(4):
            idx = x + dx[i]
            idy = y + dy[i]
            if 0 <= idx < N and 0 <= idy < N:
                if visited[idx][idy] == 0:
                    if L < abs(arr[idx][idy] - arr[x][y]) < R:
                        sum += arr[idx][idy]
                        united.append([idx, idy])
                        queue.append([idx, idy])
                    visited[idx][idy] = 1
    sum // len(united)

for i in range(N):
    for j in range(N):
        bfs(i, j)  # (0, 0) 에서 만들 수 있는 연합을 다 봄. 이어지게.