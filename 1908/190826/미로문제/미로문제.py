# 시작점과 끝점의 위치가 항상 1행은 아님. 중간일수도 있음. 제일 먼저 시작점 위치 찾기
# DFS로 풀어도됨
# 백트래킹으로 풀어도됨
# 도착할 수 있는지 여부 찾기
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
                break
    stack = []
    visited = []
    dx = [0, 0, -1, 1]  # 좌 우
    dy = [-1, 1, 0, 0]  # 상 하
    def DFS(miro, s, g):
        x, y = s, g
        stack.append((x, y))
        while stack:
            x = stack[-1][0]
            y = stack[-1][1]
            for i in range(4):
                if 0 <= dx[i] + x <= N-1 and 0 <= dy[i] + y <= N-1:  # 범위 안에 있으면
                    if miro[dx[i] + x][dy[i] + y] == 3:
                        return 1
                    if miro[dx[i] + x][dy[i] + y] == 0 and (dx[i] + x, dy[i] + y) not in visited:
                        x = dx[i] + x
                        y = dy[i] + y
                        stack.append((x, y))
                        visited.append((x, y))
                        break  # 얘를 안하니까 값이 안나오네
            else:
                stack.pop()
        return 0
    result = DFS(miro, start[0], start[1])
    print('#{} {}'.format(tc, result))