Q = [0] * 6
front = rear = -1

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

print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(enQueue(4))
print(enQueue(5))
print(deQueue())
print(enQueue(7))
print(Qpeek())

Q = [0] * 10
f = r = -1
r += 1; Q[r] = 1
r += 1; Q[r] = 2
r += 1; Q[r] = 3

f += 1; print(Q[f])
f += 1; print(Q[f])
f += 1; print(Q[f])
