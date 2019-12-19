# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     miro = [list(map(int, (map(str, input())))) for _ in range(N)]
#     dx = [0, 0, -1, 1]  # 상 하
#     dy = [-1, 1, 0, 0]  # 좌 우
#     for i in range(N):
#         for j in range(N):
#             if miro[i][j] == 2:
#                 start = [i, j]
#     print(start)
#
#     stack = []
#     visited = [[0] * (N+1) for _ in range(N+1)]
#     def DFS(stack, s, g):
#         x = s
#         y = g
#         stack.append((x, y))
#         visited[x][y] = 1
#         while stack:
#             for i in range(4):
#                 if 0 <= dx[i] + x < (N+1) and 0 <= dy[i] + y < (N+1):  # 범위 안에 있으면
#                     if miro[dx[i] + x][dy[i] + y] == 0:
#
#
#
#
#     print(DFS(stack, start[0], start[1]))