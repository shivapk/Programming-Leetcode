#this prints the strongly connected components in O(m+n) time
'''
The above algorithm calls DFS, fins reverse of the graph and again calls DFS. DFS takes O(V+E) for a graph represented using adjacency list. 
Reversing a graph also takes O(V+E) time. For reversing the graph, we simple traverse all adjacency lists.
'''
from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.vcount=v
        self.adjlist=defaultdict(list)

    def insert(self,v1,v2):
        self.adjlist[v1].append(v2)

    def topologicalsort(self):
        arr=[]
        color=['w']*(self.vcount)
        for v in range(self.vcount):
            if color[v]=='w':
                self.dfs(v,color,arr)
        return arr
    def dfs(self,v,color,arr):
        color[v]='g'
        for w in self.adjlist[v]:
            if color[w]=='w':
                self.dfs(w,color,arr)

        color[v]='b'
        arr.insert(0,v)

    def revgraph(self): #O(m+n)
        g=Graph(self.vcount)
        for i in self.adjlist:
            for j in self.adjlist[i]:
                g.insert(j,i)
        return g
            
    def scc(self):
        arr=self.topologicalsort()
        color=['w']*(self.vcount)
        newg=self.revgraph()
        scg=[1]*(newg.vcount)
        count=1
        for v in arr:
            if color[v]=='w':
                newg.dfsnew(v,color,scg,count)
                count+=1
                #print ()
        print (scg)

    def dfsnew(self,v,color,scg,count):
        color[v]='g'
        scg[v]=count
        #print (v, end=' ')
        for w in self.adjlist[v]:
            if color[w]=='w':
                self.dfsnew(w,color,scg,count)
        color[v]='b'
        
g = Graph(5)
g.insert(1, 0)
g.insert(0, 2)
g.insert(2, 1)
g.insert(0, 3)
g.insert(3, 4)
g.scc()
