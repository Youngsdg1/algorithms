import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
sum = cnt = 0
for i in range(N-1, -1, -1):
    if A[i] <= K:
        sum += A[i]
        cnt += 1
        if sum == K:
            print(cnt)
            break
