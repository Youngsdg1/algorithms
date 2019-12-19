import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    a_list = list(map(int, input().split()))
    def Hoare_partition(arr, left, right):
        p = arr[left]
        i = left
        j = right
        while i < j:
            while i < right and arr[i] <= p:
                i += 1
            while j > left and arr[j] >= p:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[j] = arr[j], arr[left]
        return j
    def Hoare_QuickSort(arr, left, right):
        if left < right:
            s = Hoare_partition(arr, left, right)
            Hoare_QuickSort(arr, left, s - 1)
            Hoare_QuickSort(arr, s + 1, right)
    Hoare_QuickSort(a_list, 0, len(a_list) - 1)
    print('#{} {}'.format(tc, a_list[n//2]))