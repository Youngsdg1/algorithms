arr = [1, 2, 3, 4, 5, -5, -2, 8, 9, 10]

cnt = False
for i in range(1, 1 << len(arr)):  # 1을 원소의 개수만큼 2진수 수로 바꾼거. 여기선 2^10 까지. 즉, 부분집합 갯수
    subset = []
    sum = 0
    for j in range(len(arr)):  # j 는 인덱스라 생각하고, 이제 인덱스 값을 출력하는것
        if i & (1 << j):  # 값이 같을때 그 j값에 해당하는 인덱스들을 함께 출력
            sum += arr[j]
    if sum == 0:
        cnt = True
if cnt:
    print(True)