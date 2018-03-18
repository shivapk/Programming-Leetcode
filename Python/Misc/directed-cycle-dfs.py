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
        
    def dfs(self):
        visited=[False]*(self.V)    #color=['white']*(self.V)
        recstack=[False]*(self.V)
        for i in range(self.V): #for disconnected graph
             if visited[i]==False:       #color[i]='white'
                  return (self.relax(i,visited,recstack))
        
    def relax(self,s,visited,recstack):
        visited[s]=True    #color[s]='grey'
        recstack[s]=True
        if (s==d)
        for v in self.graph[s]: 
            if visited[v]==False:    #if color[v]='white'
               return (self.relax(v,visited,recstack))
            elif recstack[v]==True: #color[v]='grey'
                return True
        recstack[s]=False   #color[s]='grey'
        return False
               
               
        
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print (g.dfs())