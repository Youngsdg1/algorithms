import sys
sys.stdin = open('input.txt', 'r')
import copy
N = int(input())
eq = input()
equation_copy = [0]*N
for i in range(0, N):
    if i % 2 == 0:
        equation_copy[i] = int(eq[i])
    else:
        equation_copy[i] = eq[i]
equation = copy.deepcopy(equation_copy)
print(equation_copy)
max_value = -1
def calc(num1, num2, buho):
    if buho == '+':
        num1 += num2
        return num1
    elif buho == '-':
        num1 -= num2
        return num1
    elif buho == '*':
        num1 *= num2
        return num1
    else:  # 이미 계산된 애일때. 더 뒤에 있는 계산된 값을 그대로.
        return num2

def calc_all(l):  # 쭉 계산하는거
    for i in range(0, N-2, 2):
        l[i+2] = calc(l[i], l[i+2], l[i+1])
        res = l[-1]
    return res

def dfs(i):
    global max_value
    if i+2 >= N:
        return
    else:
        while i < N - 2:
            # 부호 있는거 먼저 계산
            equation_copy[i+1] = calc(equation_copy[i-1], equation_copy[i+1], equation_copy[i])

            # 계산한 건 부호를 '0' 으로 처리
            equation_copy[i] = '0'
            i += 4
            # 괄호가 2개, 3개 일때 다 돌리기
            dfs(i)
            i -= 4
            # 그대로 계산 쭉 하기
            ans = calc_all(equation_copy)

            # 최댓값 찾기
            if max_value < ans:
                max_value = ans
            # equation_copy[i] = equation[i]
            # 원상태로 돌리기
            equation_copy[:] = equation
            equation_copy[i + 1] = calc(equation_copy[i - 1], equation_copy[i + 1], equation_copy[i])

dfs(1)
print(max_value)