import sys
sys.stdin = open('input.txt', 'r')
N, L = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

row = [i for i in zido]  # 가로 보는 식
col = [[row[i] for row in zido] for i in range(N)]  # 세로 보는 식

def runway(arr):
    count = 0
    for array in arr:  # 한 열씩 보면서  # 그 이후부터 보면서 똑같이 반복
        check = True
        for i in range(N-1):  # 한 칸씩 돌기
            if check == True:  # check 가 True 일 때만 보기
                diff = abs(array[i + 1] - array[i])  # 다음 것과 차이
                if diff == 0:  # 차이가 0 이면
                    continue
                elif diff == 1:  # 다음거와 차이가 1일때 L개 만큼이 이어져 있지 않으면 false
                    if array[i + 1] > array[i]:  # 다음께 더 큰 경우
                        if 0 <= i-L+1:  # 봐야되는 전 애들이 범위안에 있을 경우
                            for k in range(L):  # L 개 만큼이 ( 전의 거 봐야됨 )
                                if array[i] != array[i-k]:  # 같은 수가 아닐경우 false
                                    check = False
                            # for k in range(1, L+1):  # L 개 만큼이 ( 전의거의 전의거 )
                            #     if 0 <= i-L-k:
                            #         if array[i-L-k] > array[i-L]:  # L 개 전에 더 큰 수가 오면
                            #             check = False
                        else:
                            check = False
                    elif array[i + 1] < array[i]:  # 다음게 더 작은 경우
                        if i+L < N:  # 경사로 놓았을 때 범위 안에 있을 경우
                            for k in range(1, L+1):  # L 개 만큼이 ( 다음 거 봐야됨 )
                                if array[i+1] != array[i+k]:  # 같은 수가 아닐경우 false
                                    check = False
                            for k in range(1, L+1):  # L 개 만큼이 ( 다음거의 다음거 )
                                if i+L+k < N:
                                    if array[i+L+k] > array[i+L]:  # L 개 전에 더 큰 수가 오면
                                        check = False
                        else:  # 범위 밖이면 false
                            check = False
                else:  # 다음거와 차이가 0 이나 1 이 아니면 false
                    check = False
        if check == True:  # 끝까지 돌았는데도 true 면 카운트 세기
            count += 1
    return count

print(runway(row)+runway(col))