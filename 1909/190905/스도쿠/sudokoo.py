import sys
sys.stdin = open('sudokoo.txt', 'r')
for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    ans_row = 0
    for i in range(9):
        if set(arr[i]) == set(num):
            ans_row += 1

    sero = []
    Sero = []
    for i in range(9):
        for j in range(9):
            sero.append(arr[j][i])
        Sero.append(sero[i*9:(i+1)*9])

    ans_col = 0
    for i in range(9):
        if set(Sero[i]) == set(num):
            ans_col += 1

    res = []
    Res = []
    ans_sq = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for q in range(3):
                    res.append(arr[i*3+q][j*3+k])
    for i in range(9):
        Res.append(res[i*9:(i+1)*9])
    for i in range(9):
        if set(Res[i]) == set(num):
            ans_sq += 1

    if ans_col == ans_row == ans_sq:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))