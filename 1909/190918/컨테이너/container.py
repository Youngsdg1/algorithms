import sys
sys.stdin = open('input.txt', 'r')
# list.sort(reverse = True) 하면 역순으로 정렬이 됨
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())  # 화물, 트럭
    weight = list(map(int, input().split()))
    weight.sort(reverse=True)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    # 정렬해서 트럭은 0으로 만들어주고 더 짧은 리스트 길이만큼 돌리기
    res = []
    for i in range(m):
        for j in range(n):
            if truck[i] >= weight[j] and weight[j] != 0:
                res.append(weight[j])
                weight[j] = 0
                break
    print('#{} {}'.format(tc, sum(res)))