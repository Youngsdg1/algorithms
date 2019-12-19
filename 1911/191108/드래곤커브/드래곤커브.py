import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
dragon = [[0]*101 for _ in range(101)]  # 좌표 그릴 곳
# 0 1 2 3 우 상 좌 하
origin = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# 커브 방향 바뀌면 그려지는게 [ 상, 좌, 하, 우 ]
changed = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 0, 1, 2, 3 일 때 바뀌는 방향

for i in range(n):
    x, y, d, g = map(int, input().split())
    print(x, y, d, g)
    dragon[x][y] = 1  # 시작점
    dragon_d = [(x+origin[d][0], y+origin[d][1])]
    dragon[x+origin[d][0]][y+origin[d][1]] = 1  # 0 세대
    while g > 0:
        tmp = []
        print(dragon_d)
        for idx, idy in dragon_d:
            dx, dy = x + changed[idx][0], y + changed[idy][1]  # 각각의 방향에 따른 바뀐 방향들
            tmp.append((dx, dy))  # direction 에 추가
            dragon[dx][dy] = 1
        dragon_d += tmp
        g -= 1

result = 0
for i in range(100):
    for j in range(100):
        if dragon[x][y] and dragon[x+1][y] and dragon[x][y+1] and dragon[x+1][y+1]:
            result += 1

print(result)