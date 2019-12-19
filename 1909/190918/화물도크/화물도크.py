import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    time = [list(map(int, input().split()))for _ in range(n)]
    time.sort(key = lambda x:x[1])  # x의 1번 컬럼 기준으로 정렬
    print(time)
    ans = pre_end = 0
    for i in range(n):
        if pre_end <= time[i][0]:
            ans += 1
            pre_end= time[i][1]
    print('#{} {}'.format(tc, ans))


    # 배열의 역으로 입력받아 처리하는 방법도 있음