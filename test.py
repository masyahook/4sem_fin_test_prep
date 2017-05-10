m = int(input())
graph = {}
for j in range(m):
    v1, v2 = input().split()
    graph[v1] = graph.get(v1, []) + [v2]


def bfs(graph, start, path):
    used = set()
    Q = []
    used.add(start)
    Q.append(start)
    while Q:
        vertex = Q.pop(0)
        if len(path.get(start, [])) < 1 or vertex in graph.get(path.get(start, [])[-1], []):
            path[start] = path.get(start, []) + [vertex]
        for neighbour in graph.get(vertex, []):
            if neighbour not in used:
                Q.append(neighbour)
                used.add(vertex)
            else:
                path[start] = path.get(start, []) + [neighbour]
                return path
    path[start] = []
    return path

def find_shortest_cycle(graph):
    path = {}
    for node in graph:
        path = bfs(graph, node, path)
    return(min(path.values(), key=lambda x: len(x)))
res = ' '.join(map(str, find_shortest_cycle(graph)))
if len(res) == 0:
    print(-1)
else:
    print(res)