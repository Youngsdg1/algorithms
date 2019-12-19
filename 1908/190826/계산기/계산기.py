import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    N = int(input())
    p = input()
    ys = ['+', '*']
    gual = ['(', ')']
    huwee = []
    stack = []
    def priority(x):
        if x == '*':  # 연산순위 우선인 곱셈일때 1
            return 1
        elif x == '+':
            return 0
        elif x == '(' or x == ')':  # 괄호 무시하고 들어가게함
            return -1

    for i in p:
        if i not in ys and i not in gual:  # 숫자면 결과에 push
            huwee.append(int(i))
        elif i in ys:  # 연산이면
            while len(stack) > 0:
                if priority(stack[-1]) <= priority(i):  # top과 연산자 비교
                    break
                huwee.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                huwee.append(x)
    for i in huwee:
        if i not in ys and i not in gual:  # 숫자면 push
            stack.append(i)
        elif i == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 + n2)
        elif i == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 * n2)
    print('#{} {}'.format(tc, stack[0]))









