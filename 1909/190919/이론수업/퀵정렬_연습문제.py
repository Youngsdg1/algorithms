ipt_1 = [11, 45, 23, 81, 29, 34]
ipt_2 = [11, 45, 23, 81, 23, 34, 00, 22, 17, 8]
ipt_3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# 퀵 정렬은 피봇을 중심으로 정렬한다.
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
        Hoare_QuickSort(arr, left, s-1)
        Hoare_QuickSort(arr, s+1, right)

def Lomuto_partition(arr, p, right):
    x = arr[right]
    i = p - 1
    for j in range(p, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

def Lomuto_QuickSort(arr, left, right):
    if left < right:
        s = Lomuto_partition(arr, left, right)
        Lomuto_QuickSort(arr, left, s-1)
        Lomuto_QuickSort(arr, s+1, right)

Hoare_QuickSort(ipt_1, 0, len(ipt_1)-1)
Hoare_QuickSort(ipt_2, 0, len(ipt_2)-1)
Hoare_QuickSort(ipt_3, 0, len(ipt_3)-1)
print(ipt_1)
print(ipt_2)
print(ipt_3)
print()
Lomuto_QuickSort(ipt_1, 0, len(ipt_1)-1)
Lomuto_QuickSort(ipt_2, 0, len(ipt_2)-1)
Lomuto_QuickSort(ipt_3, 0, len(ipt_3)-1)
print(ipt_1)
print(ipt_2)
print(ipt_3)