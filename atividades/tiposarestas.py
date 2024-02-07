
def adj(u):
    return list(range(u))

def Check(u):
    dfs_num[u] = 'EXPLORED'

    for v in adj(u):
        if dfs_num == 'UNIVISIED': 
            print('T')
            dfs_parent[v] = u
            Check(v)
        elif dfs_num[v] == 



if __name__ == '__main__':
    dfs_num = {}
    dfs_parent = {}