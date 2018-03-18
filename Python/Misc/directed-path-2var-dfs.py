from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,s,d):
        visited=[False]*(self.v)
        path=[]
        self.relax(s,visited,path,d)
        
    def relax(self,s,visited,path,d):
        visited[s]=True
        path.append(s)
        print (path)
        #if s==d:
           #print (path)
        for v in self.graph[s]:
            if  visited[v]==False:
                self.relax(v,visited,path,d)
        path.pop()
        visited[s]=False
        
    def printpath(self,parent,d):
        if parent[d] is None:
                print (d, end=' ')
        else: 
             self.printpath(parent,parent[d])        
             print(d, end=' ')
                        
             
        
        
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
  
s = 2 ; d = 3
print ("Following are all different paths from %d to %d :" %(s, d))
g.dfs(s, d)