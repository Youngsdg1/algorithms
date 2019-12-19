def power_set_i():
    bit = [0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                print(bit)


def power_set_b():  # 모든 경우 구할땐 이 비트연산
    arr = [1, 2, 3]
    n = len(arr)
    for i in range(1 << n):
        print('{', end =' ')
        for j in range(n+1):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print('}')


def power_set_r(k):  # 가지치기 필요할때 이 백트래킹 기법
    if k == N: print(a)
    else:
        a[k] = 1; power_set_r(k + 1)
        a[k] = 0; power_set_r(k + 1)


print('부분집합 반복문')
power_set_i()

print('부분집합 바이너리 카운팅')
power_set_b()

N = 3
a = [0] * N
print('부분집합 재귀문')
power_set_r(0)