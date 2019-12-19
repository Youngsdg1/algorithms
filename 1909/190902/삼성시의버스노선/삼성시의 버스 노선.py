import sys
sys.stdin = open("input_bus.txt", "r")
for tc in range(1, int(input()) + 1):
    arr = [0] * 5001
    n = int(input())
    for i in range(n):
        A = input().split()
        for x in range(int(A[0]), int(A[1])+1):
            arr[x] += 1
    p = int(input())
    res = [0] * p
    for k in range(p):
        pn = int(input())
        res[k] = arr[pn]
    print('#{} {}'.format(tc, ' '.join(map(str, res))))