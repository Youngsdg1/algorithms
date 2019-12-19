T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    row_list = []
    col_list = []
    for n in range(100):
        arr.append(list(map(int, input().split())))
        sum_opp_r = 0
        sum_opp_l = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_opp_r += arr[j][j]
            if i + j == 99:
                sum_opp_l += arr[i][j]
        row_list.append(sum_row)
        col_list.append(sum_col)
    print('#{} {}'.format(test_case, max(max(row_list), max(col_list), sum_opp_r, sum_opp_l)))



    # 2차원 배열로 받기
    matrix = [list(map(int, input().split())) for _ in range]