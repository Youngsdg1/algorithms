import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    arr_1 = [[0] * 10 for _ in range(10)]
    arr_2 = [[0] * 10 for _ in range(10)]
    cnt = 0
    box_num = int(input())
    for n in range(box_num):
        input_list = list(map(int, input().split()))
        if input_list[-1] == 1:
            for i in range(input_list[0], input_list[2] + 1):
                for j in range(input_list[1], input_list[3] + 1):
                    arr_1[i][j] = 1
        if input_list[-1] == 2:
            for i in range(input_list[0], input_list[2] + 1):
                for j in range(input_list[1], input_list[3] + 1):
                    arr_2[i][j] = 2
    for i in range(10):
        for j in range(10):
            if arr_1[i][j] + arr_2[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))