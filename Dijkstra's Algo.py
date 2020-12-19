#Dijkstra's Algorithm


class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for col in range(vertices)] for row in range(vertices)]

    def minDist(self,d,l):
        mindist=10000

        for v in range(self.V):
            if d[v]<mindist and l[v]==False:
                mindist=d[v]
                min_index=v

        return min_index

    def showPath(self,node,src,parent):

       

        if(parent[node]==None):
            print(src)
            return

        else:
            print(node)
            self.showPath(parent[node],src,parent)

        

    


        

    def dijkstara(self,src):
        d=[10000]*self.V
        l=[False]*self.V
        d[src]=0
        parent=[-1]*self.V
        parent[src]=None

    
       

        for output in range(self.V):
             u=self.minDist(d,l)
             l[u]=True

             for v in range(self.V):
                 if(self.graph[u][v]>0 and l[v]==False and d[v]>d[u]+self.graph[u][v]):
                     d[v]=d[u]+self.graph[u][v]
                     parent[v]=u
                     


        for node in range(self.V):
            print(node,"\t",d[node])

        print(parent)


        while(True):
            print("Enter -1 to leave")
            x=int(input("Enter node to view it's path"))
            if(x==-1):
                break

            else:
                self.showPath(x,src,parent)
            
            


        


        

        



g=Graph(9)

g.graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

n=int(input("Enter source"))
        

g.dijkstara(n)

             
            
        
