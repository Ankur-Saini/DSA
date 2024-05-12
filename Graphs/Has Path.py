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
    
    # DFS Approach
    
    # def __hasPath(self, visited, v1, v2):
    #     if v1 >=self.nVertices or v2 >= self.nVertices:
    #         return False
    #     if self.containsEdge(v1, v2):
    #         return True
    #     visited[v1] = True
    #     for i in range(self.nVertices):
    #         if self.adjMatrix[v1][i] == 1 and visited[i] is False:
    #             if self.__hasPath(visited, i, v2):
    #                 return True
    #     return False
    
    # def hasPath(self, v1, v2):
    #     visited = [False for i in range(self.nVertices)]
    #     return self.__hasPath(visited, v1, v2)

    # BFS Approach

    def __hasPath(self, sv, ev, visited):
        if sv == ev:
            return True

        q = Queue()
        q.put(sv)
        visited[sv] = True

        while not q.empty():
            u = q.get()
            
            for v in range(self.nVertices):
                if self.adjMatrix[u][v] == 1 and not visited[v]:
                    if v == ev:
                        return True
                    q.put(v)
                    visited[v] = True
        return False
    
    def hasPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPath(self, sv, ev, visited)
    
    def __str__(self):
        return str(self.adjMatrix)
    
vertices, edges = [int(x) for x in input().split()]
graph = Graph(vertices)
for i in range(edges):
    v1, v2 = [int(x) for x in input().split()]
    graph.addEdge(v1, v2)
v1, v2 = [int(x) for x in input().split()]
if graph.hasPath(v1, v2):
    print("true")
else:
    print("false")
