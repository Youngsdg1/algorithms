# 갈 수 있을때까지 우, 상, 좌, 하 / 우, 하, 좌, 상 가야됨
def def_cleaner(conditioner, dust, time):
    global sum
    if time == T:  # 마지막 카운트
        for i in range(R):
            for j in range(C):
                if dust[i][j] != 0 and dust[i][j] != -1:
                    sum += dust[i][j]
        return
    else:
        # 0(확산), 1(공청위), 2(공청아래), 3(확인), 4(확산), 5(공청위), 6(공청아래), 7(확인), 8(확산) ...
        copy_arr = copy.deepcopy(dust)
        for x in range(R):  # 확산
            for y in range(C):
                if dust[x][y] != 0 and dust[x][y] != -1:
                    def_cnt = 0
                    for i in range(4):
                        idx = x + dx[i]
                        idy = y + dy[i]
                        if 0 <= idx < R and 0 <= idy < C and arr[idx][idy] != -1:
                            copy_arr[idx][idy] += (dust[x][y] // 5)  # 4방향 칸에 더하기
                            def_cnt += 1
                    copy_arr[x][y] -= ((dust[x][y] // 5) * def_cnt)

        # 확산 된 애를 청소
        cleaned_dust = copy.deepcopy(copy_arr)
        # 윗부분부터
        start = conditioner[0]
        x = start[0]
        y = start[1]
        y += 1 #  공기청정기 부분 빼고 시작
        cleaned_dust[x][y] = 0
        while 0 <= y+1 < C:  # 우
            y += 1
            cleaned_dust[x][y] = copy_arr[x][y-1]
        while 0 <= x-1 < R:  # 상
            x -= 1
            cleaned_dust[x][y] = copy_arr[x+1][y]
        while 0 <= y-1 < C:  # 좌
            y -= 1
            cleaned_dust[x][y] = copy_arr[x][y+1]
        while copy_arr[x][y] != -1:  # 하
            x += 1
            if cleaned_dust[x][y] == -1:
                break
            else:
                cleaned_dust[x][y] = copy_arr[x-1][y]

        start = conditioner[1]  # 아랫부분
        x = start[0]
        y = start[1]
        y += 1
        cleaned_dust[x][y] = 0
        while 0 <= y+1 < C:  # 우
            y += 1
            cleaned_dust[x][y] = copy_arr[x][y - 1]
        while 0 <= x+1 < R:  # 하
            x += 1
            cleaned_dust[x][y] = copy_arr[x - 1][y]
        while 0 <= y-1 < C:  # 좌
            y -= 1
            cleaned_dust[x][y] = copy_arr[x][y + 1]
        while copy_arr[x][y] != -1:  # 상
            x -= 1
            if cleaned_dust[x][y] == -1:
                break
            else:
                cleaned_dust[x][y] = copy_arr[x + 1][y]

        # 다 끝나면 time 높여서 또 돌려
        def_cleaner(conditioner, cleaned_dust, time+1)

import copy
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
conditioner = [[0, 0], [0, 0]]
k = 0
for i in range(R):
    if arr[i][0] == -1:
        conditioner[k][0] = i
        k += 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sum = 0
def_cleaner(conditioner, arr, 0)
print(sum)



