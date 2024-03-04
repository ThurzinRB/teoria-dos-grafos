class Graph:
    def __init__(self, N):
        self.AL = [[] for _ in range(N)]
        self.visited = [False] * N

    def add(self, x, y):
        self.AL[x].append(y)
        self.AL[y].append(x)

    def adj(self, x):
        return self.AL[x]

    def dfs(self, u):
        self.visited[u] = True
        for v in self.adj(u):
            if not self.visited[v]:
                self.dfs(v)


[N, M] = list(map(int, input().split()))

debts = [int(input()) for _ in range(N)]  # Debt values

myGraph = Graph(N)

for _ in range(M):
    [X, Y] = list(map(int, input().split()))
    myGraph.add(X, Y)

total_debt = sum(debts)
if total_debt != 0:
    print('IMPOSSIBLE')
else:
    myGraph.dfs(0)
    print('POSSIBLE') if myGraph.visited.count(False) == 0 else print('IMPOSSIBLE')
