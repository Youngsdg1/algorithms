import sys
sys.stdin = open('input.txt', 'r')
def perm(a, empty, visited, k, arr):
    global min_num
    if k == n:
        s = 0
        empty.append(0)
        for i in range(n):
            s += arr[empty[i]][empty[i + 1]]
        if min_num > s:
            min_num = s
        empty.pop()
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                empty.append(a[i])
                if empty[0] == 0:
                    perm(a, empty, visited, k + 1, arr)
                    empty.pop()
                    visited[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a = [i for i in range(n)]
    min_num = 999999
    perm(a, [], [0]*n, 0, arr)
    print('#{} {}'.format(tc, min_num))