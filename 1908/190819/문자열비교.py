# 뒤에서부터 비교.  text를 돌면서 해당 인덱스값이 내 키값에 없으면 통째로 한꺼번에 점프
# skip배열 몇칸만큼 옮겨줄지
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    p = input()
    t = input()
    m = len(p)
    n = len(t)
    def BruteForce(p, t):
        i = 0  # t의 인덱스
        j = 0  # p의 인덱스
        while j < m and i < n:
            if t[i] != p[j]:
                i = i - j
                j = - 1
            i = i + 1
            j = j + 1
        if j == m:
            return 1
        else:
            return 0
    print('#{} {}'.format(tc, BruteForce(p, t)))

