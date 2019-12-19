import sys
sys.stdin = open('input.txt', 'r')

def bbfs(queue):
    global zero_cnt, visited, zero_virus
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    zero_virus = 0
    x = queue[0]
    y = queue[1]
    for i in range(4):
        idx = x + dx[i]
        idy = y + dy[i]
        if 0 <= idx < N and 0 <= idy < N:
            if visited[idx][idy] == 0:
                if arr[idx][idy] == 0:
                    visited[idx][idy] = 1
                    zero_virus += 1
                elif arr[idx][idy] == 2:
                    visited[idx][idy] = 1
                    bbfs([idx, idy])

def bfs(queue):
    global zero_cnt, visited, zero_virus
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            a = queue.pop(0)
            x = a[0]
            y = a[1]
            visited[x][y] = 1
            for i in range(4):
                idx = x + dx[i]
                idy = y + dy[i]
                if 0 <= idx < N and 0 <= idy < N:
                    if visited[idx][idy] == 0:
                        if arr[idx][idy] == 0:
                            queue.append([idx, idy])
                            visited[idx][idy] = 1
                            zero_virus += 1
                        elif arr[idx][idy] == 2:
                            queue.append([idx, idy])
                            visited[idx][idy] = 1
                            bbfs([idx, idy])
        cnt += 1
        if zero_cnt == zero_virus:
            break
    if zero_cnt == zero_virus:
        print(cnt)
        return cnt
    else:
        return -1

def perm(k, s):  # 바이러스 M 개 고르는 경우의 수
    global min_value, visited, zero_virus
    if k == M:
        q = [0] * M
        for h in range(M):  # copy
            q[h] = t[h]
        visited = [[0] * N for _ in range(N)]
        zero_virus = 0
        answer = bfs(q)
        if answer < min_value:
            min_value = answer
        return
    else:
        for i in range(s, len(virus)):
            t[k] = virus[i]
            perm(k+1, i+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [0] * 10
k = zero_cnt = 0
visited = [[0] * N for _ in range(N)]
zero_virus = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus[k] = [i, j]
            k += 1
        elif arr[i][j] == 0:
            zero_cnt += 1
while 0 in virus:
    virus.remove(0)
min_value = 999999999999999
t = [0] * M
perm(0, 0)
print(min_value)