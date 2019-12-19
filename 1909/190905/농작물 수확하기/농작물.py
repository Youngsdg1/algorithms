import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    # index = []
    # for k in range(0, n//2+1):
    #     index.append(2*k+1)
    # for k in range(n//2, 0, -1):
    #     index.append(2*k-1)
    # print(index)
    x = n % 2+1
    res = []
    # for i in range(n%2+1):
    #     res.append(arr[i][x-i:x+(i+1)])
    # res.append(arr[x])
    # for i in range(n%2+2, n):
    #     res.append(arr[i][i-x:x-i])
    # print(res)
    j = 1
    for i in range(x+1):
        res.append(arr[i][x-j+1:x+j])
        j += 1
    j = 1
    for i in range(x+1,n):
        res.append(arr[i][x-j+1:x+j])
        j += 1
    print(res)