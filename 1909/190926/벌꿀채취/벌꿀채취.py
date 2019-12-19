import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())  # N*N행렬, 벌통 개수 M, 최대 양 C
    honey = [list(map(int, input().split())) for _ in range(N)]
    honey_list = []  # 채집할 수 있는 벌꿀 묶음들
    for i in range(N):
        for j in range(N-M+1):
            honey_list.append(honey[i][j:j+M])
    visited = [0 for _ in range(len(honey_list))]
    real_result = []
    def perm(honey_list, empty, visited, k, n):
        global real_result
        if k == 2:
                result = []
                for i in empty:
                    a = i
                    result.append(a)
                real_result.append(result)
        else:
            for i in range(n, len(honey_list)):
                if visited[i] == 0:
                    visited[i] = 1
                    empty.append(honey_list[i])
                    perm(honey_list, empty, visited, k+1, i)
                    visited[i] = 0
                    empty.pop()
    perm(honey_list, [], visited, 0, 0)
    print('real_result', real_result)

    delete_res = []
    def find_real(x, k):
        global delete_res
        if k == 0:
            return
        else:
            res = []
            a = x
            delete_res.append(a)
            x = x + k
            k -= 1
            return find_real(x, k)
    find_real(0, 11)

    for i in range(2, len(delete_res), 3):
        delete_res[i] = 'x'
    print(delete_res)
    real_delete_res = []
    for i in range(len(real_result)):
        for j in delete_res:
            if j != 'x':
                if i == j:
                    real_delete_res.append(real_result[i])
    print(real_delete_res)

    res_sum = 0
    for i in real_result:
        if i not in real_delete_res:
            print(i)




