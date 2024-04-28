

import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
    def __str__(self):
        return str(self.adjMatrix)
    def getPathBFS(self, sv, ev) :
        parent = dict()
        visited = [False for i in range(self.nVertices)]
        if sv == ev:
            return [ev]
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        path = list()
        
        while not q.empty():
            cv = q.get()

            for av in range(self.nVertices):
                if self.adjMatrix[cv][av] == 1 and not visited[av]:
                    q.put(av)
                    visited[av] = True
                    parent[av] = cv

                    if av == ev:
                        path.append(ev)
                        pv = ev
                        while pv in parent:
                            path.append(parent[pv])
                            pv = parent[pv]

        return path
        

# Main
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])

li = g.getPathBFS(sv, ev)

if len(li) != 0 :
	for element in li :
		print(element, end = ' ')
