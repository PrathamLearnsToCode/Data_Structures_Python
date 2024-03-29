class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 0

    def __df(self,sv,visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMatrix[sv][i]>0 and visited[i] is False):
                self.__df(i,visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__df(0,visited)

    def removeEdges(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]>0:
            return True
        else:
            return False

g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,2)
g.addEdge(0,2)
print(g.dfs())




