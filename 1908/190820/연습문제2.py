# pop할게 없는 경우, 다 검사했는데 남아있는 경우
# 여는 괄호가 나오면 stack에 push, 닫는건 pop 해서 매치가 되는지 비교/확인

l1 = '()()((()))'
l2 = '((()((((()()((()())((())))))'
s = []

def test(l):
    for i in l:
        if i == '(':
            s.append(i)
        if i == ')':
            if len(s) != 0:
                s.pop()
            else:
                return False
    if len(s) > 0:
        return False
    else:
        return True
print(test(l1))


stack = [0] * 100
top = -1
str = '()()((()))'

wrong = 0
for i in range(len(str)):
    if str[i] == '(':
        top += 1: stack[top] = str[i]
    elif str[i] == ')':

