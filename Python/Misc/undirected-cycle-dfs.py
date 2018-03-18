# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self,v):
 
        # default dictionary to store graph
        self.V=v
        self.graph = defaultdict(list)
        
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def dfs(self):
        visited=[False]*(self.V)
        parent=[None]*(self.V)
        for i in range(self.V): #for disconnected graph
             if visited[i]==False:
                  return (self.relax(i,visited,parent))
        
        
    def relax(self,s,visited,parent):
        visited[s]=True
        print (s)
        for v in self.graph[s]: 
            if visited[v]==False:
               parent[v]=s
               return (self.relax(v,visited,parent))
            elif parent[s]!=v: #returns true if found cycle
                return True
        return False
               
               
        
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
print ("Following is DFS from (starting from vertex 2)")
print (g.dfs())