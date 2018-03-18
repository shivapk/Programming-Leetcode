#say given graph is a valid tree or not.An undirected graph is tree if it has following properties.
#1) There is no cycle.
#2) The graph is connected.
#Time: O(n) where n is the number of vertices..as number of edges will be n-1.
#space: O(n) where n is number of vertices
# keep track of parent in case of undirected graph, although directed graph is not tree but if you want to find cycle for directed graph then p is not required
'''
cycle:For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already visited and u is not parent of v,
then there is a cycle in graph. If we don’t find such an adjacent for any vertex, we say that there is no cycle.
'''
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.vcount=n
        self.adjlist=defaultdict(list)
        
    def insert(self,v1,v2):
        self.adjlist[v1].append(v2)
        self.adjlist[v2].append(v1)
                
class Solution:
    def isgraph_tree(self,g):
    
        color=['w']*(g.vcount)
        #for v in range(g.vcount):#as we need to show graph is connected so need to do for every vertex
        if self.dfs(0,color,g,-1): #choose any random vertex- 0 and -1 is assumed parent of 0 #parent is not required to check cycle in directed graph
            return False
        for i in range(g.vcount): #check after dfs anything is left still not visited
            if color[i]=='w':
                return False
        return True
    
    def dfs(self,v,color,g,p): # returns True if there is any cycle in the graph, p is for parent
        color[v]='g' # grey means in process not yet backtracked to this vertex
        for w in g.adjlist[v]:
            if color[w]=='w' and self.dfs(w,color,g,v): # for directed graph p is not required
                    return True
            elif color[w]=='g' and w!=p :    # for directed graph p is not required
                    return True # cycle found
        color[v]='b' #time to backtrack
        return False # no cycle found
               
g=Graph(5)# number of vertices so nodes are labels from 0 to n-1
g.insert(1, 0)
g.insert(0, 2)
#g.insert(2,1)
g.insert(0, 3)
g.insert(3, 4)
s=Solution()
print (s.isgraph_tree(g))
