import sys
sys.stdin = open('input.txt', 'r')
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print('arr', arr)
perm_num = N * (N - 1) * (N - 2) // 6  # 순열로 나오는 경우의 수
arrow = [[0] * 3 for _ in range(perm_num)]
idx = 0

def perms(k, n, empty, visited):  # 궁수를 찾음 -> 순열로!
    global arrow, idx
    if k == 3:
        for q in range(3):
            arrow[idx][q] = empty[q]
        idx += 1
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                empty.append(i)
                perms(k + 1, i, empty, visited)
                visited[i] = 0
                empty.pop()


perms(0, N, [], [0] * N)
print('궁수의 인덱스 모든 경우의 수', arrow)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_value = 0
# 각각의 궁수의 표적을 찾음
for perm_arrow in range(perm_num):
    cnt = 0
    while 1 in sum(arr, []):  # 맨 밑에 성이 있다. 1이 다 사라질때까지 한다.
        # 궁수 먼저 공격
        for x in range(M):
            for k in range(3):
                if arr[N - 1][x] == 1 and arrow[perm_arrow][k] == x:  # 마지막 줄에 있을 경우
                    arr[N - 1][x] = 'die'  # 죽음 표시
                    cnt += 1

                    # 거리가 D 이하면서 제일 먼저 발견되는 애들
                    # 여럿일 경우 가장 왼쪽에 있는 적을 공격(위. 오 있으면 위)
        # 공격이 끝나면 한 칸 아래로 이동
        for row in range(N):
            for col in range(M):
                if arr[N - 1][row] == 1:  # 맨 밑에 있는 1은 아래로 없애버리기
                    arr[N - 1][row] = 0
                for idn in range(4):
                    idx = row + dx[idn]
                    idy = col + dy[idn]
                    if 0 <= idx < N and 0 <= idy < M:  # 밑으로 한 칸 옮기기
                        arr[idx + 1][idy] = arr[idx][idy]
                        arr[idx][idy] = 0
        if cnt > max_value:
            max_value = cnt

print(max_value)