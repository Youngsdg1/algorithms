arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(0, (1<<n)):  # 1 << n 은 부분집합의 개수. 2^n
    for j in range(0, n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):
            print('%d, '% arr[j], end='')
    print()
    # i가 7일때 어쩌꼬111 이니까 3, 6, 7 인 부분집합이 나옴

