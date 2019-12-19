import sys
sys.stdin = open('danjo.txt', 'r')

def my_find(x):
    for i in range(1, len(x)):
        if int(x[i-1]) > int(x[i]):
            return False
    return True

for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    value = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] * A[j]) >= 10 and my_find(str(A[i] * A[j])) and value < A[i] * A[j]:
                value = A[i] * A[j]
    if value == 0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, value))

