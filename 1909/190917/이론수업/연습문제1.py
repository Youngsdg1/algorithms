# 선택 정렬 함수(Selection Sort)를 재귀적 알고리즘으로 작성해 보시오.
A = [3, 4, 9, 8, 8, 9, 6, 5, 5, 1, 2]

# 반복을 이용한 선택정렬
def SelectionSort1(A):
    n = len(A)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp
    print(A)

# SelectionSort1(A)

# 재귀를 이용한 선택정렬
def SelectionSort2(A, i):
    n = len(A)
    min = i
    if min < n:
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp
        SelectionSort2(A, i+1)

def rec_SelectionSort(A, s, e):
    if s == e: return

    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j
    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s+1, e)


SelectionSort2(A, 0)
print(A)