import sys
sys.stdin = open('input.txt', 'r')


def Bbit_print(i):
    global output
    if 65 <= ord(i) <= 70:
        num = '{}'.format(ord('{}'.format(i)) - ord('A') + 10)
        a = 0
        res_1 = [0, 0, 0, 0]
        temp = int(num)
        while a != 4:
            b = temp % 2
            res_1[a] = b
            temp = temp // 2
            a += 1
        # print(res_1, end=' ')
        res_1.reverse()
        output.append(res_1)

    elif ord(i) < 65:
        a = 0
        res = [0, 0, 0, 0]
        temp = int(i)
        while a != 4:
            b = temp % 2
            res[a] = b
            temp = temp // 2
            a += 1
        res.reverse()
        output.append(res)

for tc in range(1, int(input())+1):
    n, sy = input().split()
    output = []
    for i in sy:
        Bbit_print(i)
    print('#{} {}'.format(tc, ''.join(map(str, sum(output, [])))))