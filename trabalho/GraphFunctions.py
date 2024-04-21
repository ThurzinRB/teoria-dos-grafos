# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict
 
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self, vertices):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = vertices+1
 
     

    # Function to add an edge to graph
    def addEdge(self, u, v):
        print('Adicionando ', u, ' ', v)
        self.graph[u].append(v)

     

    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in range(self.V):
            if visited[neighbour] == False:
                self.DFSUtil(neighbour, visited)
 

     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = [False]*self.V
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)



    def ToposortUtil(self,v,visited,stack):
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                self.topologicalSortUtil(neighbour,visited,stack)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)



    def Toposort(self):

        #Create stack to store order
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)



    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def Dijkstra(self, src):
        
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    
    def save_dot_file(self, filename = 'grafo.dot'):
        with open(filename, 'w') as f:
            f.write("digraph G {\n")
            for u in range(self.V):
                for v in self.graph[u]:
                    f.write(f"  {u} -> {v};\n")
            f.write("}\n")