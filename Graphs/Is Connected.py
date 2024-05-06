from queue import Queue
import sys
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
    
    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        q = Queue()
        q.put(0)
        visited[0] = True

        while not q.empty():
            cv = q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[cv][i] == 1 and not visited[i]:
                    q.put(i)
                    visited[i] = True
        
        for i in range(self.nVertices):
            if not visited[i]:
                return False
        return True
    
    
    def __str__(self):
        return str(self.adjMatrix)
    
vertices, edges = [int(x) for x in input().split()]
graph = Graph(vertices)
if vertices > 0:
    for i in range(edges):
        v1, v2 = [int(x) for x in input().split()]
        graph.addEdge(v1, v2)
    connected = graph.isConnected()
    if connected:
        print("true")
    else:
        print('false')
else:
    print('true')
