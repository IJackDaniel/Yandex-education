def dfs(start):
    global find1
    color[start] = "Grey"
    for v in graph[start]:
        if color[v] == "White":
            dfs(v)
        elif color[v] == "Grey":
            find1 = True
    color[start] = "Black"
n, m = map(int, input().split())
# n - количество участников
# m - количество игр
graph = dict()
for i in range(1, n + 1):
    graph[i] = list()
players = set()
for _ in range(m):
    u, v, t = map(int, input().split())
    players.add(u)
    players.add(v)
    # u - первый игрок в партии
    # v - второй игрок в партии
    # t - победитель в партии
    # print(u, v, t)
    t = u if t == 1 else v
    graph[u + v - t] = graph[u + v - t] + [t]
# print(graph)
players = sorted(list(players))
if len(players) == n:
    for i in range(1, n + 1):
        find1 = False
        color = ["White"] * (n + 1)
        dfs(i)
        if not find1:
            if "White" in color[1:]:
                find1 = False
            else:
                find1 = True
                break
    f1 = find1
    find2 = True
    for key in graph.keys():
        if len(graph[key]) > 1:
            find1 = False
            for l in graph[key]:
                find1 = False
                color = ["White"] * (n + 1)
                dfs(l)
                if not find1:
                    if "White" in color[1:]:
                        find1 = False
                    else:
                        find1 = True
                        break
            if not find1:
                find2 = False
    result = "YES" if f1 and not find2 else "NO"
    print(result)
else:
    print("NO")
'''
5 6
1 4 1
1 2 1
3 1 2
4 2 1
2 3 1
5 3 2
'''