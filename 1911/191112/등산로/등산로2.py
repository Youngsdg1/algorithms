import sys
sys.stdin = open('input.txt', 'r')

def iswall(x, y): return  0 <= x < N and 0 <= y < N

def dfs(x, y, l):  # 4방향 탐색하면서, 갈 수 있는 길 찾기
    global max_length, gongsa
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):  # 우, 좌, 하, 상
        idx, idy = x + dx , y + dy
        if iswall(idx, idy) and not visited[idx][idy]:
            if zido[x][y] > zido[idx][idy]:
                visited[idx][idy] = 1
                dfs(idx, idy, l + 1)
                visited[idx][idy] = 0
            else:
                if not gongsa:
                    if zido[x][y] > zido[idx][idy] - K:
                        for g in range(K):
                            zido[idx][idy] -= (g+1)
                            if zido[x][y] > zido[idx][idy]:
                                visited[idx][idy] = 1
                                gongsa = 1
                                dfs(idx, idy, l + 1)
                                visited[idx][idy] = 0
                            zido[idx][idy] += (g+1)
                            gongsa = 0
    if max_length < l:
        max_length = l

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    zido = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(sum(zido, []))

    max_height = [0] * 5
    k = 0
    for i in range(N):  # 가장 높은 지형의 좌표 리스트 뽑기
        for j in range(N):
            if zido[i][j] == max_val:
                max_height[k] = (i, j)
                k += 1
    while 0 in max_height:  # 온전히 좌표만 남기기
        max_height.remove(0)
    max_length = 0
    for x, y in max_height:
        visited = [[0] * N for _ in range(N)]
        visited[x][y] = 1
        gongsa = 0
        dfs(x, y, 1)
        visited[x][y] = 0

    print('#{} {}'.format(tc, max_length))