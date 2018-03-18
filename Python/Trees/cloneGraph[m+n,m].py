#Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors
#{0,1,2#1,2#2,2}, First node is labeled as 0. Connect node 0 to both nodes 1 and 2 SO ON..
#Time=O(m+n) as we are covering entire graph once
#space=O(m)# queue size can grow 
class UndirectedGraphNode:
     def __init__(self, x):
            self.label = x
            self.neighbors = []
                        
class Solution(object):
    def copyGraph(self, node):#runs simple traversal on original graph
        if node is None:
            return node
        root = UndirectedGraphNode(node.label)
        q = [node]
        visited = {}  #to store label as key and node object as value{0:object}
        visited[node.label] = root
        while q:
            temp = q.pop()  #current node 
            for n in temp.neighbors:#on each of the neighbor dfs is applied #n is a neighbor of temp
                if n.label not in visited:#if not visited add it to queue and place it in visited dictionary
                    q.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[temp.label].neighbors.append(visited[n.label])#if n in visited then add n as the neighbor of temp
        return root


'''
recursive Dfs type solution. Space is optimized to O(h) here(h is height), time=O(m+n)
class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def copyGraph(self, node):
        if not node:
            return None
        if node.label in self.visited:
            return self.visited[node.label]

        root = UndirectedGraphNode(node.label)
        self.visited[node.label] = root
            
        for n in node.neighbors:
            root.neighbors.append(self.copyGraph(n))
        return root

'''
node0=UndirectedGraphNode(0)
node1=UndirectedGraphNode(1)
node2=UndirectedGraphNode(2)
node0.neighbors=[node1,node2]
node1.neighbors=[node2]
node2.neighbors=[node2]
s=Solution()
#print (node0.label)
print (s.copyGraph(node0))
