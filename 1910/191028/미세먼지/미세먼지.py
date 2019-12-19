def defusion(arr): # 이 함수 한번에 확산 한번 되는거임
    copy_arr = copy.deepcopy(arr)
    for x in range(R):
        for y in range(C):
            if arr[x][y] != 0 and arr[x][y] != -1:
                def_cnt = 0
                for i in range(4):
                    idx = x + dx[i]
                    idy = y + dy[i]
                    if 0 <= idx < R and 0 <= idy < C and arr[idx][idy] != -1:
                        copy_arr[idx][idy] += (arr[x][y] // 5)   # 4방향 칸에 더하기
                        def_cnt += 1
                copy_arr[x][y] -= ((arr[x][y] // 5) * def_cnt)
    return copy_arr  # 바뀐 배열 return

# 갈 수 있을때까지 우, 상, 좌, 하 / 우, 하, 좌, 상 가야됨
def cleaner(conditioner, dust, k, time):
    global sum
    if k == 1 or k == 0:
        cleaned_dust = copy.deepcopy(dust)
        start = conditioner[k]
        x = start[0]
        y = start[1]
        if k == 0:  # 공기청정기 윗부분
            y += 1 #  공기청정기 부분 빼고 시작
            cleaned_dust[x][y] = 0
            while 0 <= y+1 < C:  # 우
                y += 1
                cleaned_dust[x][y] = dust[x][y-1]
            while 0 <= x-1 < R:  # 상
                x -= 1
                cleaned_dust[x][y] = dust[x+1][y]

            while 0 <= y-1 < C:  # 좌
                y -= 1
                cleaned_dust[x][y] = dust[x][y+1]
            while dust[x][y] != -1:  # 하
                x += 1
                cleaned_dust[x][y] = dust[x-1][y]
            cleaner(conditioner, cleaned_dust, k+1, time)
        elif k == 1:  # 공기청정기 아랫부분
            while 0 <= y+1 < C:  # 우
                y += 1
                cleaned_dust[x][y] = dust[x][y - 1]
            while 0 <= x+1 < R:  # 하
                x += 1
                cleaned_dust[x][y] = dust[x - 1][y]
            while 0 <= y-1 < C:  # 좌
                y -= 1
                cleaned_dust[x][y] = dust[x][y + 1]
            while dust[x][y] != -1:  # 상
                x -= 1
                cleaned_dust[x][y] = dust[x + 1][y]
            cleaner(conditioner, cleaned_dust, k + 1, time)
    else:
        if time == T:  # 마지막 초에만 카운트 하게
            for i in range(R):
                for j in range(C):
                    if dust[i][j] != 0 and dust[i][j] != -1:
                        sum += dust[i][j]
            return

import sys, copy
sys.stdin = open('input.txt', 'r')
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
print(R, C, T)
print(arr)
conditioner = [[0, 0], [0, 0]]
k = 0
for i in range(R):
    if arr[i][0] == -1:
        conditioner[k][0] = i
        k += 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input_arr = arr
for i in range(1, T+1):  # T 초 후 남아있는 미세먼지는 clean_dust
    dust = defusion(input_arr)
    sum = 0
    cleaner(conditioner, dust, 0, i)
    input_arr = cleaned_dust
print(sum)



