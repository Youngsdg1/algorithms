import sys
sys.stdin = open('input.txt', 'r')

# clothes = [list(input()) for _ in range(3)]
# print(clothes[0])
# from collections import Counter
# # li = Counter([c for _, c in clothes])
# # print(li)

# a = [[0,10], [1, 100], [2, 200], [3, 300]]
# print([n for _, n in a])
#  결과:  [10, 100, 200, 300]

my_dict = {}  # 빈 딕셔너리를 만든다

# 다음과 같은 리스트가 있다고 가정했을 때
l = [[1, 100], [2, 200], [3, 300], [33, 300]]

# for x, y in l:
#     my_dict[x] = y

# print(my_dict)

for x, y in l:
    if y not in my_dict:
        my_dict[y] = 1
    else:
        my_dict[y] += 1

print(my_dict)