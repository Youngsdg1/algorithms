import sys
sys.stdin = open("input.txt", "r")
#
# num = int(input())
# num_list = list(map(int, input().split()))
def view():
    result = []
    num_list = list(map(int, input().split()))
    for i in range(2, len(num_list)):
        if num_list[i] > num_list[i-1] and num_list[i] > num_list[i-2] and num_list[i] > num_list[i+1] and num_list[i] > num_list[i+2]:
            result.append(num_list[i] - max(num_list[i-1], num_list[i-2], num_list[i+1], num_list[i+2]))
            i += 3
        else:
            pass
    return sum(result)

T = 10
for tc in range(1, T+1):
    m = input()
    res = view()
    print("#{} {}".format(tc, res))