import sys
sys.stdin = open('input.txt', 'r')
def BinarySearch(target, data):
    l = 0
    r = len(data) - 1
    check = ['m']
    while l <= r:
        m = (l + r) // 2
        if data[m] == target:
            return True
        elif data[m] < target:
            l = m + 1
            if check[-1] == 'l':
                return False
            check.append('l')
        else:
            r = m - 1
            if check[-1] == 'r':
                return False
            check.append('r')
    return False

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    res = 0
    for i in B:
        if BinarySearch(i, A):
            res += 1
    print('#{} {}'.format(tc, res))