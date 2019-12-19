import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    huwee = input().split()
    stack = []
    ys = ['+', '*', '-', '/', '.']
    for i in huwee:
        if i not in ys:  # 숫자
            stack.append(int(i))
        elif i == '.':  # 끝
            if len(stack) != 1:  # '.' 이 나왔는데 stack 이 1개가 아닌경우
                print('#{} error'.format(tc))
                break
            elif len(stack) == 1:
                print('#{} {}'.format(tc, stack[0]))
        elif len(stack) >= 2:  # 연산자
            if i == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif i == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)  # - 나 / 연산은 pop 시켰을때 연산자 순서 반대
            elif i == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif i == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
        else:
            print('#{} error'.format(tc))
            break

    # 연산자가 있는데 숫자가 충분히 있는지
    # 연산자가 있는데 숫자가 부족하던지


