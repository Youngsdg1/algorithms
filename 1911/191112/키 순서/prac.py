def find_parent(x):  # 더 큰 애 찾기
    global upper_path, result_up
    for a in p[x]:  # 부모가 있으면
        if a not in upper_path:
            upper_path.append(a)  # path 에 추가
            find_parent(a)  # 걔의 부모 있나 또 보기
            upper_path.pop()
    else:  # 없으면
        for r in upper_path:
            result_up.append(r)
        return


def find_child(x):  # 더 작은 애 찾기
    global lower_path, result_dw
    for i in range(1, N+1):
        for b in p[i]:
            if b == x:
                if i not in lower_path:
                    lower_path.append(i)
                    find_child(i)
                    lower_path.pop()
    else:
        for r in lower_path:
            result_dw.append(r)
        return


N = int(input())
M = int(input())
p = [[]*(N+1) for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(M)]
for kk in range(M):
    a = arr[kk][0]
    b = arr[kk][1]
    p[a].append(b)
cnt = 0
for idx in range(1, N+1):
    result_up = []
    upper_path = []
    find_parent(idx)

    result_dw = []
    lower_path = []
    find_child(idx)

    if len(set(result_up))+len(set(result_dw)) == N-1:
        cnt += 1
print(cnt)
