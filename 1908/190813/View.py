import sys
sys.stdin = open("input.txt", "r")

num = int(input())
num_list = list(map(int, input().split()))

result = []
def find(num, num_list):
    for i in range(1, num - 1):
        if num_list[i-1] != 0 and abs(num_list[i] - num_list[i-1]) >= 2 and abs(num_list[i] - num_list[i+1]) >= 2 and num_list[i+1] != 0:
            result.append(abs(int(num_list[i] - num_list[i-1])))
        else:
            pass
    return sum(result)

T = 10
for tc in range(1, T+1):
    N =int(input())
    H = list(map(int, input().split()))

    print("#%d %d" % (tc, find(num, num_list)))