import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = float(input())
    jarisu = len(str(n))-2
    ans = ""
    temp = n * 2
    while temp != 0:
        ans += str(int(temp))
        temp = (temp-int(temp)) * 2
        if len(ans) > 13:
            print('#{} {}'.format(tc, 'overflow'))
            break
    if len(ans) < 13:
        print('#{} {}'.format(tc, ans))