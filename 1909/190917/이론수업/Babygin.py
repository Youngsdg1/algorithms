# baby_gin 완전검색으로 순열 만들어서 하기
arr = list(map(int, input().split()))
cnt = 0
def perm(arr, n, k):
    global cnt
    if k == n:
        if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
            if arr[3] == arr[4] == arr[5]:
                cnt = 1
            elif arr[3]+1 == arr[4] and arr[4]+1 == arr[5]:
                cnt = 1
        elif arr[0] == arr[1] == arr[2]:
            if arr[3]+1 == arr[4] and arr[4]+1 == arr[5]:
                cnt = 1
            elif arr[3] == arr[4] == arr[5]:
                cnt = 1
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, n, k+1)
            arr[k], arr[i] = arr[i], arr[k]
perm(arr, len(arr), 0)

if cnt == 1:
    print('baby gin')
else:
    print('no')