import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    real_res = []
    def perm(arr, visited, empty, k):
        global real_res
        if k == N:
            res = []
            for i in range(len(empty)):
                res.append(empty[i])
            real_res.append(res)
        else:
            for i in range(N):
                if visited[i] == 0:
                    empty.append(i)
                    visited[i] = 1
                    perm(arr, visited, empty, k+1)
                    visited[i] = 0
                    empty.pop()
    perm(arr, [0]*N, [], 0)
    min_value = 9999999999999
    sum_fact = 0
    print(real_res)
    k = 0
