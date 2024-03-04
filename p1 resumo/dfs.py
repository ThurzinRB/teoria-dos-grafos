
visitado = [0]*len(V)
def r_dfs(u):
    visitado[u] = 1
    for v in adj(u):
        if visitado[v] == 0:
            r_dfs(v)      