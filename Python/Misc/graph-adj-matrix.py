class Node:
    def __init__(self,name):
        self.name=name

class Graph:
    graph={} #has node names and values pointing to the Node
    matrix=[] #has 0 and 1s
    matrix_indices={}
    def add_node(self,u):
        if isinstance(u,Node) and u.name not in self.graph:
            self.graph[u.name]=u
            for i in self.matrix:
                i.append(0)
            self.matrix.append([0]*(len(self.matrix)+1)) #replace with len(self.matrix[0])
            self.matrix_indices[u.name]=len(self.matrix_indices)
    
    def add_edge(self,u,v,weight=1):
        if u in self.graph and v in self.graph:
            self.matrix[self.matrix_indices[u]][self.matrix_indices[v]]=weight
            self.matrix[self.matrix_indices[v]][self.matrix_indices[u]]=weight
    def print_graph(self):
        for vertex,index in sorted(self.matrix_indices.items()):
            print(vertex + ' ', end='')
            for j in range(len(self.matrix)):
                print (self.matrix[index][j],end=" ")
            print (' ')
                
                 
            
                          
            
            

g=Graph()
a=Node('A')
b=Node('B')
c=Node('C')
d=Node('D')
e=Node('E')
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

edges=['AB','BC','BD','AC','CE','CD','DE']
for i in edges:
    #g.add_node(Node(i[:1]))
    #g.add_node(Node(i[1:]))
    g.add_edge(i[:1],i[1:])
    

g.print_graph()
