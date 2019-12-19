import sys
sys.stdin = open('input.txt', 'r')

def iswall(x, y): return  0 <= x < N and 0 <= y < N

def dfs(x, y):  # 4방향 탐색하면서, 갈 수 있는 길 찾기
    global length
    queue = [(x, y)]
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    gongsa = 0
    path = [[0]*3 for _ in range(4)]  # 각 4 방향에 대한 길들의  path list 저장
    t = 0
    kx, ky = queue.pop()
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):  # 우, 좌, 하 상
        nx, ny = kx + dx, ky + dy
        if iswall(nx, ny) and not visited[nx][ny] and zido[kx][ky] > zido[nx][ny]:
            visited[nx][ny] = 1
            queue.append((nx, ny))
            while queue:
                for nx, ny in queue:
                    for idx, idy in (0, 1), (0, -1), (1, 0), (-1, 0):  # 한 방향에서 갈 수 있는 길 쭉 봤을 때
                        inx, iny = nx + idx, ny + idy
                        if iswall(inx, iny) and not visited[inx][iny]:
                            if zido[nx][ny] > zido[inx][iny]:
                                queue.append((inx, iny))
                                visited[inx][iny] = 1
                                path[t] = inx, iny, zido[inx][iny]
                            elif zido[nx][ny] > zido[inx][iny] - K:  # 높이를 1보다 작게 만드는게 가능하댔으므로 띠로 조건 X
                                queue.append((inx, iny))  # 공사가 딱 1번만 가능하므로, 일단 다 리스트를 만들고 경우의 수 보기
                                visited[inx][iny] = 1
                                path[t] = inx, iny, zido[inx][iny]
        t += 1
    print(path)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    zido = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N):  # 가장 높은 높이 찾기
        for j in range(N):
            if zido[i][j] > max_val:
                max_val = zido[i][j]

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
    for y, x in max_height:
        length = 0
        dfs(y, x)
        if length > max_length:
            max_length = length
    print('#{} {}'.format(tc, max_length))