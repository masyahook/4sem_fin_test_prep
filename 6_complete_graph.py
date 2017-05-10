n, m = list(map(int, input().split()))
graph = [[0] * n for i in range(n)]
for i in range(m):
    v1, v2 = list(map(int, input().split()))
    v1, v2 = v1 - 1, v2 - 1
    graph[v1][v2] = graph[v2][v1] = 1
ext = False
for i in range(n):
    for j in range(1 + i, n):
        if graph[i][j] == 0:
            print('NO')
            ext = True
            break
    if ext:
        break
else:
    print('YES')
