# push, pop, peek, empty 구현. 임의로 데이터 3개 넣고 꺼내는걸로.

s = []
def push(item):
    s.append(item)

def pop():  # top의 위치값을 체크하는일이 꼭 들어가야됨
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

def peek(s):
    if len(s) == 0:
        return
    else:
        return s[-1]

def isEmpty(s):
    if len(s) == 0:
        return 'empty'
    else:
        return 'Not empty'

top = 0
for i in range(3):
    s[top + 1] = i
    top += 1
    
for i in range(3):
    t = s[top]
    top -= 1
