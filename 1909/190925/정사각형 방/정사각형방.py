import sys
sys.stdin = open('input.txt', 'r')
def bfs(a, b):
    global cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [b, a]
    visited = [[0] * N for _ in range(N)]
    visited[b][a] = 1
    while queue:
        cnt += 1
        for _ in range(len(queue)//2):
            x = queue.pop()
            y = queue.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if visited[ny][nx] == 0 and A[ny][nx] == A[y][x] + 1:
                        visited[ny][nx] = 1 + visited[y][x]
                        queue.append(ny)
                        queue.append(nx)

for tc in range(1, int(input())+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    res = []
    max_value = 0
    min_value = 99999999
    cp = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            bfs(j, i)
            if cnt >= max_value:
                max_value = cnt
                res.append(cnt)
                cp.append((j, i))

    result = []
    for i in range(N):
        for j in range(N):
            for k in range(len(cp)):
                if cp[k][0] == j and cp[k][1] == i:
                    cnt = 0
                    bfs(j, i)
                    if cnt == max(res):
                        result.append(A[i][j])

    print('#{} {} {}'.format(tc, min(result), max(res)))