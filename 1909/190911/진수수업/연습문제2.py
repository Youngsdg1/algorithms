# 16진수를 2진수로 바꿔서 10진수로 바꾸기
import sys
sys.stdin = open('input.txt', 'r')
inp = input()
put = []
for i in inp:
    put.append(i)
output = []
print('put', len(put))
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
        output += res_1

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
        output += res
        # print('{}'.format(int(output, 2)), end=' ')


def print_10(nums):
    length = len(put)
    for k in range(4*length//7+1):
        if k <= 4*length//7-1:
            result = 0
            for i in range(6, -1, -1):
                result += int(nums.pop(0)) * (1 << i)
            else:
                print(result, end=' ')
        else:
            res_0 = 0
            for i in range(len(nums)-1, -1, -1):
                res_0 += int(nums.pop(0)) * (1 << i)
            else:
                print(res_0, end=' ')

for i in put:
    Bbit_print(i)
print(output)
print(print_10(output))
