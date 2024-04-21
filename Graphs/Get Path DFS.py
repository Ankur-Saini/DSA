

# Write your code here
# Write your code here
from queue import Queue
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
    
    
    def __getPath(self, sv, ev, visited):
        if sv == ev:
            return [ev]
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                path = self.__getPath(i, ev, visited)
                if path is not None:
                    path.append(sv)
                    return path
        return None
    
    def getPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        path = self.__getPath(sv, ev, visited)
        if path is None:
            return
        for v in path:
            print(v, end = " ")
    
    
    def __str__(self):
        return str(self.adjMatrix)
    
vertices, edges = [int(x) for x in input().split()]
graph = Graph(vertices)
for i in range(edges):
    v1, v2 = [int(x) for x in input().split()]
    graph.addEdge(v1, v2)
sv, ev = [int(x) for x in input().split()]
graph.getPath(sv, ev)
