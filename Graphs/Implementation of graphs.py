class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for i in range(vertices)] for j in range(vertices)]

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __str__(self):
        return str(self.adjMatrix)

g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
print(g)



