#DFS twice so T=O(n) as its a tree m+n=n-1+n=2n
#space=O(n)
'''logic-We start DFS from a random node and then see which node is farthest from it. 
Let the node farthest be X. It is clear that X will always be a leaf node and a corner of DFS. Now if we start DFS from X and check the 
farthest node from it, we will get the diameter of the tree.
'''
from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.vcount=v
        self.adjlist=defaultdict(list)
        
    def addedge(self,v1,v2):
        self.adjlist[v1].append(v2)
        self.adjlist[v2].append(v1)
        
def diameter(g):
    countmax=[-1] #diameter of the tree
    c=0
    color=([0]+['w']*(g.vcount))
    leaf=[1]
    leaf=dfs(g,1,c,color,countmax,leaf)  #farthest leaf from 1
    color=([0]+['w']*(g.vcount))
    dfs(g,leaf[0],c,color,countmax,leaf)  #farthest leaf from this leaf
    return countmax[0]
    

def dfs(g,v1,c,color,countmax,leaf):
    color[v1]='b' 
    if c>countmax[0]:
        countmax[0]=c
        leaf[0]=v1
    for w in (g.adjlist[v1]):
        if color[w]=='w':
            dfs(g,w,c+1,color,countmax,leaf)        
    return leaf
        
g=Graph(9)
g.addedge(1,2)
g.addedge(1,3)
g.addedge(2,4)
g.addedge(2,5)
g.addedge(4,7)
g.addedge(7,8)
g.addedge(5,6)
g.addedge(6,9)
print (diameter(g))
