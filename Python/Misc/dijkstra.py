import sys
class Graph():
    def __init__(self,vertices):
        self.v=vertices
        self.matrix=[[0]*v]*v
        
    def minimum(self,dist,explored):
        min=sys.maxint
        for i in range(self.v):
            if (dist[i]<min) and explored[i]=False:
               min=dist[i]
               index=i
        return index
           
                  
    def dijkstra(self,src):
        dist=[sys.maxint]*(self.v)  # all are at infinity
        dist[src]=0
        parent=[None]*(self.v)
        explored=[False]*(self.v)
        for i in range(self.v):
            u=self.minimum(dist,explored) //pop
            explored[index]=True
            for v in range(self.v):
                if self.matrix[u][v]>0 and explored[v]=False and dist[index]>dist[v]+
             
       
g=Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];
 
g.dijkstra(0);       