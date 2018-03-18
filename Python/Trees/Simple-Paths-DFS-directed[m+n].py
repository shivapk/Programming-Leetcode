#O(m+n) simple paths in directed graph using dfs
#Simple path is a path which do not have repeting vertices
from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.vcount=v
        self.adjlist=defaultdict(list)

    def insert(self,v1,v2):
        self.adjlist[v1].append(v2)


    def dfs(self,v,v2,color,path):
        color[v]='g'
        path.append(v)
        if v==v2:
            print (path)
        else:
            for e in self.adjlist[v]:
                if color[e]=='w':
                    self.dfs(e,v2,color,path) #recursive call
                    '''cycle
                elif color[e]=='g':
                    print ('cycle')
                    '''
                    
        color[v]='w'  #so that this can be reached again
        path.pop()

    def allpaths(self,v1,v2):
        color=['w']*(self.vcount)
        path=[]
        self.dfs(v1,v2,color,path)
                        
    '''        
    def printpath(self,p,curr):
        if p[curr]==-1:
            print (curr,end='')
            return 
        self.printpath(p,p[curr])
        print ('->',curr,end='')
    '''
'''        
g= Graph(6)
g.insert(5, 2)
g.insert(5, 0)
g.insert(4, 0)
g.insert(1, 4)
g.insert(2, 3)
g.insert(3, 1)
#g.insert(3,5)
g.allpaths(5,0)

'''
g= Graph(4)
g.insert(0, 1)
g.insert(0, 2)
g.insert(0, 3)
g.insert(2, 0)
g.insert(2, 1)
g.insert(1, 3)
g.allpaths(2,3)


