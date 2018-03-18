#time complexity is O(n+m) where n number of vertices and m number of edges
#Longest path in directed acyclic graph
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

    def longpath(self):
        torder=self.topologicalSort()
        d=[float('-inf')]*(self.vcount)
        s=torder[0]
        d[s]=0
        p=[-1]*(self.vcount)
        for v in torder:
            '''if target is given
            if v==1:
                return self.printpath(p,v)
                if not given then below only below code'''
            for w in self.adjlist[v]:
                if d[w]<d[v]+1:
                    d[w]=d[v]+1
                    p[w]=v
        ''' print path iteratively
        target=d.index(max(d))
        curr=target
        while curr!=-1:
            print (curr,end='<-')
            curr= p[curr]
        print (None)
        '''
        target=d.index(max(d))
        self.printpath(p,target)
        
        return d  #no need to return if you done ant distances

    def printpath(self,p,curr):
        if p[curr]==-1:
            print (curr,end='')
            return
        self.printpath(p,p[curr])
        print ('->',curr,end='')
            
g= Graph(6)
g.insert(5, 2)
g.insert(5, 0)
g.insert(4, 0)
g.insert(4, 1)
g.insert(2, 3)
g.insert(3, 1)
#g.insert(3,5)
#print ('\n',g.longpath())
g.longpath()
