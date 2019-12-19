import sys
sys.stdin = open('input.txt', 'r')
def bfs(queue):
    global zero_cnt, min_value
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = zero_virus = 0
    visited = [[0] * N for _ in range(N)]
    flag = True
    while queue and flag == True:
        cnt += 1
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
                            if zero_cnt == zero_virus:
                                flag = False
                                if cnt < min_value:
                                    min_value = cnt
                                    return
                                break
                        elif arr[idx][idy] == 2:
                            visited[idx][idy] = 1
                            queue.append([idx, idy])
    return

def perm(k, s):  # 바이러스 M 개 고르는 경우의 수
    global min_value
    if k == M:
        q = [0] * M
        for h in range(M):  # copy
            q[h] = t[h]
        bfs(q)
        return
    else:
        for i in range(s, len(virus)):
            t[k] = virus[i]
            perm(k+1, i+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [0] * 10
k = zero_cnt = 0
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
if min_value == 999999999999999 and zero_cnt != 0:
    print(-1)
elif zero_cnt == 0:
    print(0)
else:
    print(min_value)