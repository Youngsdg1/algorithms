import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def find_parent(x):  # 더 큰 애 찾기
    global upper_path, result_up
    if not p[x]:
        for r in upper_path:
            if r not in result_up:
                result_up.append(r)
        return
    else:
        for a in p[x]:  # 부모가 있으면
            if a not in upper_path:
                upper_path.append(a)  # path 에 추가
                find_parent(a)  # 걔의 부모 있나 또 보기
                upper_path.pop()


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
            if r not in result_dw:
                result_dw.append(r)
        return


for tc in range(1, int(input()) + 1):
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
        result_up = deque()
        upper_path = deque()
        find_parent(idx)
        print(idx, '보다 큰애', result_up)

        result_dw = deque()
        lower_path = deque()
        find_child(idx)
        print(idx, '보다 작은애', result_dw)

        if len(result_up)+len(result_dw) == N-1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
