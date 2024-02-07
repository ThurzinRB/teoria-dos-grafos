# Aula 2

## Operações básicas de grafos

- new(v): cria um grafo retorna void
- put(v): insere vértice retorna coir
- adj(u): retorna lista de vértices adjacentes
- conn(u,v): verifica se u e v estão conectados retorna bool

## [Grafo simples vs Grafo completo](https://www.inf.ufsc.br/grafos/definicoes/definicao.html#:~:text=Um%20grafo%20%C3%A9%20dito%20ser,seus%20v%C3%A9rtices%20tem%20grau%203.&text=Um%20grafo%20%C3%A9%20dito%20ser%20completo%20quando%20h%C3%A1%20uma,cada%20par%20de%20seus%20v%C3%A9rtices.)


## Tipos abstrados de dados em estudo:


- Matriz de adjacência (MA)
- Lista de adjacência (AL)
- Lista de aresta (EL)

Para cada estutura acima, foram verificadas as ordens de cada operação em um grafo simples

vazio|AL|MA|EL
|---------|-------------|--------|------| 
|new(v)   |  O(v)       |O(1)    |O(1)     |
|put(v)   |O(grau(v))   |O(1)    |O(\|E\|)     |
|adj(v)   |  O(1)       |O(\|v\|)| O(\|E\|)     |
|conn(u,v)|O(grau(u))   |O(1)    |  O(\|E\|)    |
