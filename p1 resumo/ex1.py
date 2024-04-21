class graph:
    def __init__(self, N):
        self.grafo = [[] for _ in range(N)]
        self.visited = [False]*N
    
    def add(self, u,v):
        self.grafo[u-1].append(v-1)
        self.grafo[v-1].append(u-1)
    
    def dfs(self, u):
        self.visited[u] = True
        for v in self.adj(u):
            if not self.visited[v]:
                self.dfs(v)
        
            
    def adj(self, v):
        return self.grafo[v]
    
    def unvisited(self):
        result = []
        for i in range(len(self.visited)):
            if not self.visited[i]:
                result.append(i+1)
        return result

[N, M] = list(map(int, input().split()))
#N: nodes
#M: edges
myGraph = graph(N)
for i in range(M):
    [a, b] = list(map(int, input().split()))
    # print(a,b)
    myGraph.add(a,b)

myGraph.dfs(0)
result = myGraph.unvisited()
if len(result)==0:
    print('Connected')
else:
    print(*result, sep ='\n')

    
    
