class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [0 for i in range(self.nVertices) for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def hasPath(self,v1,v2):
        if self.adjMatrix[v1][v2]>0 or self.adjMatrix[v2][v1]>0:
            return True
        