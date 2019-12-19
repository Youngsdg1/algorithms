import sys
sys.stdin = open('input.txt', 'r')


def rotate_queue(x, y):
    x.sort()
    queue = []
    waiting = []
    cnt = 0
    while x:
        count = 0
        for i in range(len(x)):  # 정렬 된 상태에서 -1씩 해준다.
            x[i] -= 1
        if queue:  # 큐 가 존재할 때
            for k in range(len(queue)):  # 값을 하나씩 빼준다.
                queue[k] -= 1
            while 0 in queue:  # queue에 있는 0을 다 없애준다.
                queue.remove(0)
        for i in range(len(x)):  # 어차피 맨 앞부터 0이 되기 때문에,
            if x[i] == 0:
                count += 1
        if count > 0:  # 하나라도 0이 있는 경우에만
            for i in range(count):  # 0이 있는 갯수를 센 만큼 pop 해준다.
                x.pop(0)
                if len(queue) < 3:  # 계단의 칸수 만큼을 queue 에 넣어준다.
                    queue.append(y)
                else:  # 3개가 넘어가면 waiting 에 넣어준다.
                    waiting.append(0)
        while len(queue) < 3:  # 큐가 3개 이하인데
            if waiting:  # waiting 이 있으면
                queue.append(y)  # 큐에 추가
                waiting.pop(0)  # waiting 에서 pop
            else:
                break
        cnt += 1
    while waiting:  # waiting 에 뭔가 남아있을 수 있음 ...
        for k in range(len(queue)):  # 값을 하나씩 빼준다.
            queue[k] -= 1
        while 0 in queue:  # queue에 있는 0을 다 없애준다.
            queue.remove(0)
        if len(queue) < 3:  # 큐에 공간이 있을 때
            while len(queue) < 3 and waiting:
                waiting.pop()
                queue.append(y)
        cnt += 1
    return cnt + y


def pre_rotate(stair_1, stair_2):
    ans_1 = ans_2 = 0
    if len(stair_1) > 3 and len(stair_2) <= 3:
        ans_1 = rotate_queue(stair_1, stair_num[0])  # rotate_queue 는 길이가 3 이상인 애들만 돌리기
        if len(stair_2) > 0:
            ans_2 = max(stair_2) + stair_num[1]
        ans = max(ans_1, ans_2)

    elif len(stair_2) > 3 and len(stair_1) <= 3:
        ans_2 = rotate_queue(stair_2, stair_num[1])
        if len(stair_1) > 0:
            ans_1 = max(stair_1) + stair_num[0]
        ans = max(ans_1, ans_2)

    elif len(stair_1) > 3 and len(stair_2) > 3:
        ans = max(rotate_queue(stair_1, stair_num[0]), rotate_queue(stair_2, stair_num[1]))

    else:  # 두 계단 가는 경우의 수가 둘 다 3 이하인 경우
        if len(stair_1) > 0:
            ans_1 = max(stair_1) + stair_num[0]
        if len(stair_2) > 0:
            ans_2 = max(stair_2) + stair_num[1]
        ans = max(ans_1, ans_2)
    return ans + 1





def powerset(k, n):
    global t, min_value
    if k == n:  # 중복순열
        stair_1 = []
        stair_2 = []
        for j in range(cnt):  # 사람 번째 인덱스에 각각 계단으로 가는 시간 구하기
            if t[j] == 0:
                stair_1.append(time[j][0])
            else:
                stair_2.append(time[j][1])
        answer = pre_rotate(stair_1, stair_2)  # 그 경우일때의 최종 시간 구하기
        if answer < min_value:  # 대소비교
            min_value = answer
        return
    else:
        for i in range(2):
            t[k] = i
            powerset(k + 1, n)

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = cnt = 0
    stair = [(0, 0), (0, 0)]
    stair_num = [0, 0]
    for i in range(N):  # 계단 찾기
        for j in range(N):
            if arr[i][j] != 1 and arr[i][j] != 0:
                stair[k] = (i, j)
                stair_num[k] = arr[i][j]
                k += 1
            elif arr[i][j] == 1:  # 사람 수 찾기
                cnt += 1
    k = 0
    time = [[0, 0] for _ in range(cnt)]
    for i in range(N):  # 거리 찾기
        for j in range(N):
            if arr[i][j] == 1:
                time[k][0] = abs(i-stair[0][0]) + abs(j-stair[0][1])
                time[k][1] = abs(i-stair[1][0]) + abs(j-stair[1][1])
                k += 1
    t = [0] * cnt
    min_value = 99999999999
    powerset(0, cnt)
    print('#{} {}'.format(tc, min_value))