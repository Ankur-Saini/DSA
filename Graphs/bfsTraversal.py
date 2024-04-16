


from queue import Queue

class Graph():
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self, v1, v2):
        return self.adjMatrix[v1][v2] == 1
    
    # def _bfsHelper(self, sv, q, visited):
    #     while not q.empty():
    #         v1 = q.get()
    #         for i in range(n):
    #             if self.adjMatrix[v1][i] == 1 and visited[i] == 0:
    #                 print(i, end = " ")
    #                 q.put(i)
   
    def bfs(self, sv):
        visited = [0 for i in range(self.nVertices)]
        q = Queue()
        print(sv, end = " ")
        q.put(sv)
        visited[sv] = 1
        while not q.empty():
            v1 = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[v1][i] == 1 and visited[i] == 0:
                    print(i, end = " ")
                    q.put(i)
                    visited[i] = 1
            

input_list = [int(x) for x in input().split()]
n = input_list[0]
e = input_list[1]

if n > 0:
    g = Graph(n)
    for i in range(e):
        vertices = [int(x) for x in input().split()]
        v1 = vertices[0]
        v2 = vertices[1]
        g.addEdge(v1, v2)
    if e > 0:
        g.bfs(0)
    else:
        for i in range(n):
            print(i, end = " ")




