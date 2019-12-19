Q = [0] * 20
front = rear = -1
N = 0
def isFull():
    return rear == len(Q) -1

def isEmpty():
    return front == rear

def Qpeek():
    return Q[-1]

def enQueue(item):
    global rear
    if isFull():
        return 'Full'
    else:
        rear += 1
        Q[rear] = item
        return Q[front+1:rear+1]

def deQueue():
    global front
    if isEmpty():
        return 'Empty'
    else:
        front += 1
        return Q[front]
t = 0
total_cchu = 1
N = 1
while total_cchu < 20:
    N += 1  # N = 1, 12, 123, 1234, 12345 이런식
    for i in range(1, N+1):
        new_cchu = rear
        total_cchu += i * new_cchu
        t += N
        enQueue(N)
        d = deQueue(enQueue(N))
        print('큐에 있는 사람 수 : {}'.format(len(enQueue(i))))
        print('현재 일인당 나눠주는 사탕의 수 : {}'.format(int(total_cchu / N)))
        print('현재까지 나눠준 사탕의 수 : {}'.format(total_cchu))
        print('---------------------------------')