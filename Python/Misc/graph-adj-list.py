class Node:
    def __init__(self,name):
        self.name=name
        self.neighbors=[]

    def add_neighbor(self,v):
        self.neighbors.append(v)
        self.neighbors.sort()


class Graph:
    graph={}
    
    def add_node(self,u):
        if isinstance(u,Node) and u.name not in self.graph:
            self.graph[u.name]=u
            
    def add_edge(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u].add_neighbor(v)
            self.graph[v].add_neighbor(u)
    def print_graph(self):
        for key in self.graph:
            print (key +'->'+ str(self.graph[key].neighbors))
    

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
    
        
