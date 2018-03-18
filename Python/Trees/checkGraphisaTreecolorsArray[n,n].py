#say given undirected graph is a valid tree or not.An undirected graph is tree if it has following properties.
#1) There is no cycle.
#2) The graph is connected.
'''
cycle:For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already visited and u is not parent of v,
then there is a cycle in graph. If we don’t find such an adjacent for any vertex, we say that there is no cycle.
'''
#Time: O(n) where n is the number of vertices..as number of edges will be n-1.
#space: O(n) where n is number of vertices
# keep track of parent in case of undirected graph, for directed graph p is not required
from collections import defaultdict
        
class Solution:
    def isgraph_tree(self,n,arr):
        if len(arr)==0:  #corner case
            return True
        adjlist=defaultdict(list)
        for v1,v2 in arr:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        color=['w']*(n)
        #for v in range(n):#as we need to show graph is connected so need to do for every vertex
        if self.dfs(0,color,adjlist,-1): #choose any random vertex- 0 and -1 is assumed parent of 0
            return False
        for i in range(n): #check after dfs anything is left still not visited
            if color[i]=='w':
                return False
        return True
    
    def dfs(self,v,color,adjlist,p): # returns True if there is any cycle in the graph, p is for parent
        color[v]='g' # grey means in process not yet backtracked to this vertex
        for w in adjlist[v]:
            if color[w]=='w' and self.dfs(w,color,adjlist,v): # for directed graph p is not required
                    return True
            elif color[w]=='g' and w!=p :    # for directed graph p is not required
                    return True # cycle found
        color[v]='b' #time to backtrack
        return False # no cycle found

#arr=[[0,1],[1,2],[2,3],[1,3],[1,4]]
arr=[[0,1],[0,2],[0,3],[1,4]]
n=5 # number of vertices so nodes are labels from 0 to n-1
s=Solution()
print (s.isgraph_tree(n,arr))
