from queue import Queue
import sys
sys.setrecursionlimit(10**6)
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
    
    # BFS approach
    def bfsConnected(self):
        visited = [False for i in range(self.nVertices)]
        graphs = list()
        for v in range(self.nVertices):
            if not visited[v]:
                q = Queue()
                li = list()
                q.put(v)
                visited[v] = True

                while not q.empty():
                    cv = q.get()
                    li.append(cv)

                    for i in range(self.nVertices):
                        if self.adjMatrix[cv][i] == 1 and not visited[i]:
                            q.put(i)
                            visited[i] = True
                
                li.sort()
                graphs.append(li)
            
        return graphs 
    
    # DFS Approach
    def __connected(self, v, visited):
        li = [v]
        visited[v] = True

        for i in range(self.nVertices):
            if self.adjMatrix[v][i] == 1 and not visited[i]:
                sub_graph = self.__connected(i, visited)
                for j in sub_graph:
                    li.append(j)
        li.sort()
        return li

    def connected(self):
        visited = [False for i in range(self.nVertices)]
        graphs = list()

        for i in range(self.nVertices):
            if not visited[i]:
                graphs.append(self.__connected(i, visited))
        return graphs
    
    def __str__(self):
        return str(self.adjMatrix)

vertices, edges = [int(x) for x in input().split()]
graph = Graph(vertices)
for i in range(edges):
    v1, v2 = [int(x) for x in input().split()]
    graph.addEdge(v1, v2)
if vertices > 0:
    components = graph.connected()
    for li in components:
        for i in li:
            print(str(i), end = " ")
        print()
