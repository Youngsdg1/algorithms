import sys
sys.stdin = open('danjo.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    danjo = []
    for i in range(N):
        for j in range(i+1, N):
            danjo.append(A[i] * A[j])

    res = []
    for i in range(len(danjo)):
        x = danjo[i]
        cnt = wrong = 0
        while x // 10 != 0:
            if x % 10 < (x // 10) % 10:
                wrong += 1
                break
            elif x % 10 > (x // 10) % 10:
                x = x // 10
                cnt += 1
        if wrong == 0 and cnt == 0:  # 한자리수
            pass
        elif wrong > 0 == 0:  # 틀렸을 경우
            pass
        elif danjo[i] % (cnt*100) == danjo[i]:
            res.append(danjo[i])
    if res == []:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, max(res)))