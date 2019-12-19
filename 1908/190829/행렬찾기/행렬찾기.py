import sys
sys.stdin = open("input.txt", "r")
import copy
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * (n + 2) for _ in range(n + 1)]
    fake_arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    arr[1:n] = fake_arr
    arr_1 = copy.deepcopy(arr)
    start = []
    end = []
    for i in range(n):
        for j in range(n):
            if arr_1[i][j] != 0:
                arr_1[i][j] = 0
                if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                    start_x = i
                    start_y = j
                    start.append((start_x, start_y))
                if arr_1[i][j+1] == 0 and arr_1[i+1][j] == 0:
                    end_x = i
                    end_y = j
                    end.append((end_x, end_y))
    print('s', start)
    print('e', end)
    # result = []
    # for i in range(len(start)):
    #     hang = end[i][0] - start[i][0] + 1  # 행
    #     yeol = end[i][1] - start[i][1] + 1  # 열
    #     result.append((hang, yeol))
    # print(result)

