import sys
sys.stdin = open('input.txt', 'r')

def is_wall(room, x, y):
    return x < 0 or y < 0 or x >= N or y >= N or room[x][y] == 0


def find_group(room, x, y, visited):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(x, y)]
    path = []
    while q:
        cur = q.pop(0)
        if not visited[cur[0]][cur[1]]:
            path.append(room[cur[0]][cur[1]])
            visited[cur[0]][cur[1]] = 1
        for vector in direction:
            next_x, next_y = cur[0] + vector[0], cur[1] + vector[1]
            if not is_wall(room, next_x, next_y) and not visited[next_x][next_y]:
                if abs(room[next_x][next_y] - room[cur[0]][cur[1]]) == 1:
                    q.append((next_x, next_y))

    return [len(path), min(path)]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_move_count = 0
    min_num = N

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move_count, num  = find_group(room, i, j, visited)
                print(move_count, num)
                if move_count > max_move_count:
                    max_move_count = move_count
                    min_num = num
                elif move_count == max_move_count and min_num > num:
                    min_num = num

    print('#{} {} {}'.format(t, min_num, max_move_count))