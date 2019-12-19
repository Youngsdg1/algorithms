import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    text = input()
    def peek(s):
        if len(s) == 0:
            return
        else:
            return s[-1]
    def find(text):
        s = []
        for i in text:
            if i == '(':
                s.append(i)
            if i == ')':
                if len(s) > 0 and peek(s) == '(':
                    s.pop()
                else:
                    return 0
            if i == '{':
                s.append(i)
            if i == '}':
                if len(s) > 0 and peek(s) == '{':
                    s.pop()
                else:
                    return 0

        if len(s) > 0:
            return 0
        else:
            return 1

    print('#{} {}'.format(tc, find(text)))