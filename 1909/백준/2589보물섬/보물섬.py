import sys
sys.stdin = open('bomul.txt', 'r')
sero, garo = map(int, input().split())
bomul_map = [list(input()) for _ in range(sero)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue_list = []
max_dis = 0
for i in range(sero):
    for j in range(garo):
        if bomul_map[i][j] == "L":
            queue_list.append([i, j])
def search_bomul(que):
    dis = -1
    queue = [que]
    visited = [[False] * garo for _ in range(sero)]
    visited[que[0]][que[1]] = True
    while queue:
        dis += 1
        for _ in range(len(queue)):
            a = queue.pop(0)
            for i in range(4):
                y = a[0]
                x = a[1]
                idy = y + dy[i]
                idx = x + dx[i]
                if 0 <= idy < sero and 0 <= idx < garo:
                    if visited[idy][idx] == False:
                        if bomul_map[idy][idx] == "L":
                            visited[idy][idx] = True
                            queue.append([idy, idx])
    return dis
for que in queue_list:
    temp = search_bomul(que)
    if temp > max_dis:
        max_dis = temp
print(max_dis)