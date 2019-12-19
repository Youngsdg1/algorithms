arr = [
    ['a', 'b', 3]
    ['a', 'c', 4]
    ['b', 'd', 5]
    ['c', 'b', 1]
    ['c', 'd', 4]
    ['c', 'e', 5]
    ['d', 'e', 3]
    ['d', 'f', 4]
    ['e', 'a', 3]
    ['a', 'f', 5]
]

alpha = ['a', 'b', 'c', 'd', 'e', 'f']

def Dijkstra(s, A, D):
    u = [s]
    for v
    while u != v:
        D[w] < v-u
        u = [w]
        

        for v in arr[v]:
            D[v] = min(D[v], D[w], A[w, v])

