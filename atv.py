class Grafo:
    def __init__(self, n):
        self.grafo = []*n
    
    def adiciona_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def adj(self, u):
        return self.grafo[u]

    def BFS(self, s):

        visitados = [False]*(len(self.grafo))

        queue = []

        queue.append(s)
        visitados[s] = True
        cores = {}
        cor = False
        cores.append({s: cor})

        while queue:
            s = queue.pop(0)
            cores[s] = cor

            for i in self.grafo[s]:
                if i not in cores:
                    if cores[s] == False:
                        cor = True
                    else: cor = False
                    cores[i] = cor
                    queue.push(i)
                else:
                    if cores[i] == cores[s]:
                        print("NOT BICOLORABLE")
            
            print("BICOLORABLE")
            

                

            

        

while(True):
    try:
        n = int(input())
        l = int(input())

        graph = Grafo(n)

        for i in range(n):
            
            [u, v] = list(map(int, input().split()))

            graph.adiciona_aresta(u,v)

            graph.BFS

    except EOFError:
        break

    
        
        