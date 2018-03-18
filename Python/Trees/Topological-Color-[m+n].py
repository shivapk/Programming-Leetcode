#time complexity is O(n+m) as it is same as DFS
#Topological sorting of Directed acyclic graph
from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.vcount=v
        self.adjlist=defaultdict(list)

    def insert(self,v1,v2):
        self.adjlist[v1].append(v2)

    def topologicalSort(self):
        res=[]
        color=['w']*(self.vcount)
        for v in range(self.vcount):
            if color[v]=='w':
                self.dfs(v,color,res)
        return res

    def dfs(self,v,color,res):
        color[v]='g'
        for e in self.adjlist[v]:
            if color[e]=='w':
                self.dfs(e,color,res)
                '''cycle
            elif color[e]=='g':
                print ('cycle')
                '''
        color[v]='b'
        res.insert(0,v)
        
               
g= Graph(6)
g.insert(5, 2)
g.insert(5, 0)
g.insert(4, 0)
g.insert(4, 1)
g.insert(2, 3)
g.insert(3, 1)
#g.insert(3,5)
print (g.topologicalSort())
