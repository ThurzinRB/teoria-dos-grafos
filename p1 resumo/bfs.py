
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