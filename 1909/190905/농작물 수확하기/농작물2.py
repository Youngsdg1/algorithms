import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    middle = (n-1) // 2
    rev = 0
    j = 0
    for i in range(middle+1):
        start = middle - i
        end = middle + i + 1
        rev += sum(arr[j][start:end])
        j += 1

    for i in range(middle, 0, -1):
        start = middle - i+1
        end = middle + i
        rev += sum(arr[j][start:end])
        j += 1

    print('#{} {}'.format(tc, rev))



