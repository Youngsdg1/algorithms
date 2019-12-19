import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 0, 1]  # 가장 위에 있는 물고기, 중 가장 왼쪽에 있는 물고기 먹는다. ( 먹으면 빈칸 ) 먹은횟수 + 1
dy = [0, -1, 1, 0]
if sum(sum(space, [])) == 9:  # 물고기가 하나도 없을 때
    print(0)
else:
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:  # 아기 상어의 위치를 잡고, 2로 바꿔준다.
                space[i][j] = 2
                shark = [[i, j]]
                shark_size = 2
                break
        if space[i][j] == 9:
            break
    fish_cnt = 0
    flag = True
    while flag:
        baby = shark.pop(0)
        x = baby[0]
        y = baby[1]
        for i in range(4):  # 상좌우하로 이동하면서
            idx = x + dx[i]
            idy = y + dy[i]
            if 0 <= idx < N and 0 <= idy < N:
                if space[idx][idy] > space[x][y]:  # 자신보다 큰 물고기면 못지나감
                    continue
                elif space[idx][idy] == space[x][y]:  # 같은크기 물고기면 움직이긴함
                    space[x][y] = 0
                    space[idx][idy]
                    shark.append([idx, idy])  # 위치만 바꾸고 pass
                elif space[idx][idy] == 0:  # 0 이면
                    space[x][y] = 0
                    space[idx][idy] = shark_size
                    shark.append([idx, idy])  # 위치만 바꾸고 pass
                    continue
                elif space[idx][idy] < space[x][y] and space[idx][idy] != 0:  # 자신보다 작은 물고기가 있으면
                    # 먹고 빈칸으로 만든다. 먹은 횟수 + 1
                    space[idx][idy] = 0
                    fish_cnt += 1
                    space[x][y] = 0
                    shark.append([idx, idy])
            if fish_cnt == shark_size:  # 자신의 현재 크기와 먹은 개수가 같아지면 아기상어의 크기를 1 증가시킨다.
                shark_size += 1
                space[x][y] = 0
                shark.append([idx, idy])
        for i in sum(space, []):  # 아기상어보다 작은 수의 물고기가 배열에 없을 때 끝낸다.
            if i < shark_size:
                break
        else:
            flag == False