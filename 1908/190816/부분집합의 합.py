import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    n_subset = []
    cnt = 0
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(1, 1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])

        if len(subset) == n:
            if sum(subset) == k:
                cnt += 1
    print('#{} {}'.format(tc, cnt))