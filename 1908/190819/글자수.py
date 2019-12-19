import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    t = list(input())
    p = list(input())
    cnt_l = []
    for i in set(t):
        cnt_l.append(p.count(i))

    # count = {}
    # for ch in p:
    #     if ch in count:
    #         count[ch] += 1
    # max(count.values())
    print('#{} {}'.format(tc, max(cnt_l)))