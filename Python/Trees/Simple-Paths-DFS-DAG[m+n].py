#O(m+n) simple paths in directed acyclic graphs using topological sorting
#Simple path is a path which do not have repeting vertices
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

    def simplepaths(self,v1,v2):
        torder=self.topologicalSort()
        pcount=[0]*(self.vcount)
        pcount[v2]=1
        for v in torder[::-1]:
            for w in self.adjlist[v]:
                pcount[v]+=pcount[w]
            if v==v1:
                return pcount[v]
        return False #means no such vertex v1 in the graph
                        
    '''        
    def printpath(self,p,curr):
        if p[curr]==-1:
            print (curr,end='')
            return 
        self.printpath(p,p[curr])
        print ('->',curr,end='')
    '''
        
g= Graph(6)
g.insert(5, 2)
g.insert(5, 0)
g.insert(4, 0)
g.insert(4, 1)
g.insert(2, 3)
g.insert(3, 1)
#g.insert(3,5)
print ('\n',g.simplepaths(5,0))
