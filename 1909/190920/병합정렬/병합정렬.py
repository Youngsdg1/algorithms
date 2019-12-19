# list slicing 하면 시간이 오래걸림. 인덱스로 해야함
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
def merge(left, right):
    global cnt
    result = []
    i = 0
    j = 0
    if left[-1] > right[-1]:
        cnt += 1
    while (i<len(left)) and (j<len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i<len(left)):
        result.append(left[i])
        i += 1
    while (j<len(right)):
        result.append(right[j])
        j += 1
    return result

import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, mergesort(arr)[N//2], cnt))