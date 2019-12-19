import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, T + 1):
#     m = int(input())
#     n = list(map(int, input().split()))
#
#     arr = []
#     for idx in range(0, len(n) + 2, 2):
#         fake_arr = n[idx:idx + 2]
#         if arr:
#             arr.append(fake_arr)
#     print(arr)
#     #
#     # def find_back(a, x):  # 2차원 배열을 돌면서, 연결할 수 있는 값들 찾기
#     #     for i in range(len(a)):  # 2차원 배열 행들을 돌면서
#     #         if a[x][i]#지금 현재 리스트의 인덱스앞값 == l[i][1]:  # 0번째 인덱스가 어떤 리스트의 1번째 인덱스와 같다면 리턴
#     #             return l[i]  # 리스트를 통째로 쌍으로 출력
#     #
#     # def find_front(l):
#     #     for i in range(len(l)):  # 2차원 배열 행들을 돌면서
#     #         if find_back(l, 4) == l[0][i]  # 1번째 인덱스가 어떤 리스트의 0번째 인덱스와 같다면 리턴
#     #
#     #
#     # for idx in range(m):
#     #
#     #     if real_arr[idx][0] ==  # 다른 행의 두번째 인덱스랑 같다면 => 다른행을 다 돌면서 찾아줘야됨
#     #         # real_arr[idx][0] 앞에 그 인덱스 쌍을 추가해줌
#     #         # 없을때까지 실행
#     #
#     #     if real_arr[idx][1] == #다른 행의 첫번째 인덱스랑 같다면 => 다른행을 다 돌면서 찾아줘야됨
#     #         # real_arr[idx][1] 뒤에 그 인덱스 쌍을 추가해줌
#     #         # 없을때까지 실행
#     #
#     #     # 제일 길이가 긴 인덱스 행을 출력해줌
#     #

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    screws = [data[i:i + 2] for i in range(0, len(data) - 1, 2)]
    end = []

    for odd in data:
        if data.count(odd) == 1:
            end.append(odd)
    screws_2 = []
    for a in range(len(screws)):
        if screws[a][0] in end:
            screws_2 += screws[a]
            screws.pop(a)
            break

    for _ in range(N):
        for screw in screws:
            if screw[0] == screws_2[-1]:
                screws_2 += screw
                screws.pop(screws.index(screw))

    print('#{} {}'.format(tc, ' '.join(map(str, screws_2))))


