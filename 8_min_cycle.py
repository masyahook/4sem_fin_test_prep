def read_graph(e):
    graph = {}
    for i in range(e):
        v1, v2 = input().split()
        graph[v1] = graph.get(v1, []) + [v2]
    return graph


def find_min_cycle(graph):
    min_time = float('+inf')
    suitable_path = []
    for vertex in graph:
        path = {}
        used = {vertex}
        queue = [(vertex, 0)]
        path[vertex] = [vertex]
        while queue:
            current, time = queue.pop(0)
            time += 1
            if time >= min_time:
                break
            for neighbour in graph.get(current, []):
                if neighbour not in used:
                    queue.append((neighbour, time))
                    used.add(neighbour)
                    path[neighbour] = path[current] + [neighbour]
                elif neighbour == vertex:
                    min_time = time
                    suitable_path = path[current] + [vertex]
                    break
            path.pop(current)
    return suitable_path

path = find_min_cycle(read_graph(int(input())))
if path:
    print(' '.join(map(str, path)))
else:
    print(-1)
