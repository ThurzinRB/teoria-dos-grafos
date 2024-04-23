# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict
import graphviz
import heapq
 
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self, vertices, name='view'):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = vertices+1
        self.view = graphviz.Digraph(name, filename='trabalho/'+name+'.dot')
        for v in range(self.V):
            self.view.node(str(v))
 
     

    # Function to add an edge to graph
    def addEdge(self, u, v, xp = 1):
        self.view.edge(str(u), str(v), label=str(xp))
        self.graph[u].append([v, xp])
        
    def visualize(self):
        self.view.view()
     

    # A function used by DFS
    def DFSUtil(self, v, visited, visitedIndexes):
 
        # Mark the current node as visited
        visited[v] = True
        visitedIndexes.append(v)
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if visited[neighbour[0]] == False:
                self.DFSUtil(neighbour[0], visited, visitedIndexes)
                
    
 

     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = [False]*self.V
        visitedIndexes = []
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited, visitedIndexes)
        
        return visitedIndexes


    def ToposortUtil(self,v,visited,stack, transposed):
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in transposed[v]:
            if visited[neighbour[0]] == False:
                self.ToposortUtil(neighbour[0],visited,stack, transposed)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)

    def transpose(self):
        transposed_graph = defaultdict(list)
        for u in range(self.V):
            for v in self.graph[u]:
                transposed_graph[v[0]].append(u)
        return transposed_graph

    def Toposort(self):
        transposed = self.transpose()
        #Create stack to store order
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.ToposortUtil(i,visited,stack, transposed)
                
        return stack



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

    def getDist(self, u, v):
        dist = self.graph[u]
        dist = [pair[1] for pair in dist if pair[0] == v]
        if dist:
            return dist[0]
        else:
            return 1e7
    
    def biggestPath(self, src:int):
        oposite = []
        oposite = [[i[0], -i[1]] for i in self.graph]
    
    def shortestPath(self, src: int):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
 
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
 
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
 
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.graph[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        return dist
                    
    def isSorted(self, userList:list):
        visited = []
        transposed = self.transpose()
        for v in userList:
            visited.append(v)
            for neighbor in transposed[v]:
                if neighbor in visited:
                    return False
        return True
    
                  
    def save_dot_file(self, filename):
        with open(filename, 'w') as f:
            f.write("digraph G {\n")
            for u in range(self.V):
                f.write(f"  {u};\n")  # Write each vertex
                for v in self.graph[u]:
                    f.write(f"  {u} -> {v};\n")  # Write each edge
            f.write("}\n")