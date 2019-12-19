# 완전검색
def dfs(arr, path, visited, res):
    global min_num
    if sum(visited) == n:
        res += arr[path[-1][0]]
        if min_num > res:
            min_num = res
    else:
        prior = path[-1]
        for i in range(n):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                res += arr[path[-1][0]]
                path.append(i)

import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    visited[0] = 1
    min_num = 99999
    res = 0
    dfs(arr, [0], visited, res)


