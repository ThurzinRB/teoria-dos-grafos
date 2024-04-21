# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict
 
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
     
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
     
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        visited.add(v)
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in range(self.V):
            if visited[neighbour] == False:
                self.DFSUtil(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v, visited):
 
        # Create a set to store visited vertices
        visited[v] = True
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    def ToposortUtil(self,v,visited,stack):
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
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
