import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    length, start = map(int, input().split())
    fake_node_list = list(map(int, input().split()))

    node_list = []
    for i in range(0, length, 2):
        node_list.append(fake_node_list[i:i+2])

    queue = []
    for i in range(length//2):
        if node_list[i][0] == start:
            queue.append(node_list[i])

    last_nodes = []
    real_last_nodes = []
    def bfs():  # s = 방문하는 간선
        global queue, last_nodes, real_last_nodes
        gansun_visited = []
        node_visited = []
        while queue:
            last_nodes = []
            for _ in range(len(queue)):
                a = queue.pop(0)
                gansun_visited.append(a)
                node_visited.append(a[0])
                print('1', node_visited)
                for i in range(length//2):
                    if node_list[i][0] == a[1] and node_list[i] not in gansun_visited:
                        queue.append(node_list[i])
                        gansun_visited.append(node_list[i])
                        node_visited.append(a[1])
                        print('2', node_visited)
                        if node_list[i][1] not in node_visited:
                            last_nodes.append(node_list[i])
                            real_last_nodes = last_nodes
        print(real_last_nodes)
    bfs()
    max_res = 0
    for i in range(len(real_last_nodes)):
        if max_res < real_last_nodes[i][1]:
            max_res = real_last_nodes[i][1]
    print('#{} {}'.format(tc, max_res))