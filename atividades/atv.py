class Grafo:
    def __init__(self, n):
        self.grafo = [[] for _ in range(n)]
    
    def adiciona_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def BFS(self, s):
        queue = [s]
        cores = {}
        cores[s] = False

        while queue:
            s = queue.pop(0)

            for i in self.grafo[s]:
                if i not in cores and i not in queue:
                    cores[i] = not cores[s]
                    queue.append(i)
                elif cores[i] == cores[s]:
                    return "NOT BICOLORABLE"
            
        return "BICOLORABLE"

while True:
    try:
        n = int(input())
        l = int(input())

        graph = Grafo(n)

        for _ in range(l):
            u, v = map(int, input().split())
            graph.adiciona_aresta(u, v)

        print(graph.BFS(0))

    except EOFError:
        break
