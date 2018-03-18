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
        
    def bfs(self,s,d):
        visited=[False]*(self.V)  
        queue=[]
        queue.append(s)
        visited[s]=True
        while len(queue)>0:
            u=queue.pop(0)
            for i in (self.graph[u]):
                if visited[i]==False:
                    visited[i]=True
                    if i==d:
                        return True
                    else:
                         queue.append(i)
               
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print (g.bfs(2,1))