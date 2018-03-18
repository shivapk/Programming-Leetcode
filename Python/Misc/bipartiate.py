'''
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] \
                                for row in range(V)]
 adjacency matrix
 '''
 
 
 #there should not be any self loop
 #alternative should be red blue colors
from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self):
        visited=[False]*(self.v)
        color=[-1]*(self.v)
        for s in range(self.v):
            if visited[s]==False:
                color[s]=1
                queue=[]
                queue.append(s)
                while queue:
                    u=queue.pop(0)
                    for v in self.graph[u]:
                        if v==u:
                            return  False
                        if visited[v]==False:
                            visited[v]=True
                            color[v]= 1-color[u]
                            queue.append(v)
                        elif color[u]==color[v]:
                            return False
                    
        return True
                    
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(2, 3)
g.addEdge(2, 1)
g.addEdge(4,5)
g.addEdge(5,5)
print (g.bfs())