import copy
for tc in range(1, 11):
    v, e = map(int, input().split())  # 정점, 간선의 총 수
    arr = [[0] * (v+1) for _ in range(v+1)]  # v*V 행렬
    empty_arr = [[0] * (v+1) for _ in range(v+1)]
    gansun = list(map(int, input().split()))
    for i in range(0, len(gansun), 2):
        dep, arrive = gansun[i], gansun[i+1]
        arr[dep][arrive] = 1  # 인접 행렬 / 행:출발 / 열:도착

    def makecol(x):  # 가로 세로 바꾼 행렬
        x_sero = copy.deepcopy(x)
        for i in range(v+1):
            for j in range(v+1):
                if i > j:
                    x_sero[i][j], x_sero[j][i] = x[j][i], x[i][j]
        return x_sero

    def findstart(y):  # 시작점 찾기
        start = []
        for i in range(1, v+1):
            if sum(y[i]) == 0:
                start.append(i)
        return start

    result = []
    while arr != empty_arr:  # arr 모두 0 이 될 때 까지
        stt = findstart(makecol(arr))
        # result.append(stt)  # 시작점인 애들을 result에 추가
        for i in range(1, v+1):
            for j in range(1, v+1):
                if arr[i][j] == 1 and i in stt:
                    if i not in result:  # 출발점
                        result.append(i)
                    #if j not in result:
                        #esult.append(j)  # 출발점일 때 도착점을 result에 추가
                    arr[i][j] = 0  # 간선 삭제

    for i in range(1, v+1):
        if i not in result:
            result.append(i)
    result = ' '.join(map(str, result))
    print('#{} {}'.format(tc, result))