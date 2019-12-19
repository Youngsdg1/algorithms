import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    files = list(map(int, input().split()))
    result = []
    ans = files[M]
    index = [i for i in range(N)]
    print('index', index)
    print('files', files)
    cnt = 0
    while files:
        a = files[0]
        flag = True
        for i in range(len(files)):
            if a < files[i]:
                flag = False
                break
        if flag:
            result.append(a)
            cnt += 1
            if a == ans and index[files.index(a)] == M:
                print(cnt)
            files.remove(a)
            if len(files) > 1:
                index.remove(files.index(a))
        else:
            index.remove(files.index(a))
            files.remove(a)
            files.append(a)
            index.append(files.index(a))
