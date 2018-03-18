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
        
    def dfs(self,s,d):
        visited=[False]*(self.V)
        parent=[None]*(self.V)
        self.relax(s,visited,parent,d)
        self.printpath(parent,d)
        print ('\n',parent)
        
    def relax(self,s,visited,parent,d):
        visited[s]=True
        for v in self.graph[s]: 
            if visited[v]==False:
               parent[v]=s
               if (v==d):
                   return False
               else:
                   self.relax(v,visited,parent,d)
               
    def printpath(self,parent,j):
             if parent[j] is None:
                 print (j,end=' ')
                 return
             self.printpath(parent,parent[j])
             print (j,end=' ')
              
                        
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
print ("Following is DFS from (starting from vertex 2)")
g.dfs(1,4)