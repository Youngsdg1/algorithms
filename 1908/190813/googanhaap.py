import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    def my_func():
        i = 0
        result = []
        for x in range(n - m + 1):
            result.append(sum(numbers[i:i + m]))
            i += 1
        return max(result) - min(result)

    print('#{} {}'.format(test_case, my_func()))


# teachers
def find(n, m):
    maxV = 0
    minV = 1000000
    for i in range(0, n - m + 1):
        #s=sum(v[i:i + m]
        s = 0
        for j in range(i, i+m):
            s = s + v[j]
        if sum > maxV:
            maxV = s
        if s < minV:
            minV = s
    return maxV = minV

# teachers 2
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    v = list(map(int, input().split()))

    def find(n, m):
        sum = 0
        for i in range(0, m):
            sum += v[i]
        minV = sum
        maxV = sum
        for i in range(1, n - m + 1):
            sum = sum - v[i -1] + v[i + m -1]
            if sum > maxV:
                maxV = sum
            if sum < minV:
                minV = sum
        return maxV - minV
