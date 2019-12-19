import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    def my_func():
        d = int(input())
        height = list(map(int, input().split()))

        for i in range(d):
            height[height.index(max(height))] = (max(height) - 1)
            height[height.index(min(height))] = (min(height) + 1)
        return max(height) - min(height)

    print('#{} {}'.format(test_case, my_func()))


# teachers


