from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) 
        self.v = vertices 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self):
       visited=[False]*(self.v)
       sorted=[]
       for s in range(self.v):
            if visited[s]==False:
                  self.relax(s,visited,sorted)
       print (sorted)
    def relax(self,s,visited,sorted):
         visited[s]=True
         print (s)
         for v in (self.graph[s]):
              if visited[v]==False:
                  self.relax(v,visited,sorted)
                  
         sorted.insert(0,s)
         
                   
        
g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print ("Following is a Topological Sort of the given graph")
g.dfs()