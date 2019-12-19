import sys
sys.stdin = open('input.txt', 'r')
def change(k , cnt, number):
    global ans
    if cnt == 0:
        ans = max(ans, int(''.join(number)))
        return
    else:
        for i in range(k, len(number)):
            for j in range(i+1, len(number)):
                if int(number[i]) <= int(number[j]):
                    number[i], number[j] = number[j], number[i]
                    change(i, cnt-1,number)
                    number[i], number[j] = number[j], number[i]

for tc in range(1, int(input())+1):
    pan, chg_str = input().split()
    arr = [i for i in pan]
    chg = int(chg_str)
    ans = 1
    change(0, chg, arr)
    print('#{} {}'.format(tc, ans))