def read_graph(v, e):
    graph = [[] for i in range(v)]
    for i in range(e):
        v1, v2 = list(map(int, input().split()))
        v1 -= 1
        v2 -= 1
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


def is_bipart(graph, v, states=None):
    non_used = {i for i in range(v)}
    if states is None:
        states = [None] * v
    while non_used:
        current = non_used.pop()
        queue = [current]
        states[current] = True
        while queue:
            current = queue.pop(0)
            rep = states[current] ^ True
            for neighbour in graph[current]:
                if neighbour in non_used:
                    non_used.remove(neighbour)
                    queue.append(neighbour)
                    states[neighbour] = rep
                elif states[neighbour] != rep:
                    return False
    return True

n, m = list(map(int, input().split()))
my_graph = read_graph(n, m)
st = [None] * n
if is_bipart(my_graph, n, st):
    print('YES')
    print(' '.join(map(str, [i + 1 for i in range(n) if st[i] is True])))
else:
    print('NO')
