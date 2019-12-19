import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    T = int(input())
    square = [[0] * 100 for i in range(100)]
    for i in range(100):
        square[i] = list(input())
    pal_row = [0] * 100
    pal_col = [0] * 100
    print(square)
    def find(square):
        n = a = j = b = 0
        for i in range(100):
            if j < 50:
                b = a
                for k in range(50):
                    if square[i][j:j+k] == square[i][j:j+k][::-1]:
                        a = k
                        if b > a:
                            a = a
                        elif a > b:
                            a = b
                    else:
                        pass
            pal_row[n] = a
            n += 1
            j += 1  # j가 하나 늘었을때의 k 값을 비교해서 a에 더 큰값을 넣어야됨



        print(pal_row)
        # sero = square
        # for i in range(100):
        #     for j in range(100):
        #         if i > j:
        #             sero[i][j], sero[j][i] = sero[j][i], sero[i][j]
        # m = b = 0
        # for i in range(100):
        #     pal_col[m] = b
        #     m += 1
        #     for j in range(50):
        #         for k in range(50):
        #             if sero[i][j:j + k] == sero[i][j:j + k][::-1]:
        #                 b = k
        #             else:
        #                 pass
        # print(pal_col)
    print('#{} {}'.format(tc, find(square)))