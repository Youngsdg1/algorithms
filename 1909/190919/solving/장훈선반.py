import sys
sys.stdin = open('input.txt', 'r')
def powerset(k):
    if k == n:
        if sum(t) >= b:
            res.append(sum(t) - b)
    else:
        t[k] = height[k]
        powerset(k + 1)  # 선택하지 않은 상태에서 그 다음 단계로 넘어감
        t[k] = 0
        powerset(k + 1)  # 선택하고 넘어감
for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    t = [0] * n
    res = []
    powerset(0)
    print('#{} {}'.format(tc, min(res)))