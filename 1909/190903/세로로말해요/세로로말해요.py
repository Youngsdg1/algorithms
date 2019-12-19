import sys
sys.stdin = open('sero.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [list(map(str, input())) for _ in range(5)]
    length = []
    for i in range(5):
        length.append(len(arr[i]))
    x = max(length)
    for i in range(5):
        if len(arr[i]) < x:
            for _ in range(x-len(arr[i])):
                arr[i].append('00')
    sero = []
    for i in range(x):
        for j in range(5):
            if arr[j][i] != '00':
                sero.append(arr[j][i])
    print('#{} {}'.format(tc, ''.join(sero)))

    # try:
    #     result +=
    # except IndexError:
    #     pass