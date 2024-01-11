

class Graph:

    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for i in range(self.nVertices)]

    def addEdge(self,v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2):
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return self.adjMatrix[v1][v2] == 1
    
    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)
    
    def __str__(self):
        return str(self.adjMatrix)
    
graph1 = Graph(5)
graph1.addEdge(0,1)
graph1.addEdge(2,3)
graph1.addEdge(4,4)
print(graph1)
print(graph1.containsEdge(1,0))
graph1.removeEdge(2,3)



print(graph1)
graph1.addEdge(2,1)
graph1.dfs()
