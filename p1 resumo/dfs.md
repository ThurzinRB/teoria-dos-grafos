# DFS

## com recursão


```py
visitado = [0]*len(V) # V são todos os vértices do grafo criamos um array de não visitados
def r_dfs(u):
    visitado[u] = 1 # marca aquele vértice como visitado
    for v in adj(u): # pra cada vizinho, se ainda não estiver visitado executa um dfs dele
        if visitado[v] == 0:
            r_dfs(v)
```

## sem recursão

```py
visitado = [0]*len(V)
def dfs(u):
    fila = []
    fila.append(u)
    while (len(fila)!=0):
        v = fila.pop()
        if visitado[v] == 0:
            visitado[v] = 1
            for i in adj(v):
                if visitado[i] == 0:
                    fila.append(i)
```
# BFS

```py
visitado = [0]*len(V)
def bfs(u):
    Q = [u]
    while len(Q) != 0: #enquanto a fila não estiver vazia
        u = Q[0]
        Q.pop(0)
        for v in adj(u):
            if visitado[v] == 0:
                Q.push(v)
            else:
                continue
```

