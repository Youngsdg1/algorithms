import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())  # N*N행렬, 벌통 개수 M, 최대 양 C
    honey = [list(map(int, input().split())) for _ in range(N)]
    honey_list = []  # 채집할 수 있는 벌꿀 묶음들
    for i in range(N):
        for j in range(N-M+1):
            honey_list.append(honey[i][j:j+M])
    print(honey_list)
    for i in range(len(honey_list)):
