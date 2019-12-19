import sys
sys.stdin = open('input.txt', 'r')
def BinarySearch(target, data):
    l = 0
    r = len(data) - 1
    while l <= r:
        m = (l + r) // 2

        if data[m] == target:
            return m
        elif data[m] < target:
            l = m + 1
        else:
            r = m - 1
    return
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())   # 심사대 수, 받아야되는 사람 수
    tk = [0] * N
    for i in range(N):
        tk[i] = int(input())  # 걸리는 시간 리스트
    print(sorted(tk))
    BinarySearch()
