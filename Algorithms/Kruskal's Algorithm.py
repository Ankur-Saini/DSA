
class Edge():
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def getParent(v, parent):
    if parent[v] == v:
        return v
    return getParent(parent[v], parent)

def kruskals(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key = lambda edge: edge.wt + edge.src)
    count = 0
    output = []
    i = 0

    while count < (nVertices - 1):
        currEdge = edges[i]
        srcParent = getParent(currEdge.src, parent)
        destParent = getParent(currEdge.dest, parent)
        if srcParent != destParent:
            output.append(currEdge)
            count += 1
            parent[srcParent] = destParent
        i += 1
    return output

v, e = [int(x) for x in input().split()]
edges = list()
for i in range(e):
    src, dest, wt = [int(x) for x in input().split()]
    edge = Edge(src, dest, wt)
    edges.append(edge)
output = kruskals(edges, v)
for edge in output:
    if edge.src < edge.dest:
        print(str(edge.src) + " " + str(edge.dest) + " " + str(edge.wt))
    else:
        print(str(edge.dest) + " " + str(edge.src) + " " + str(edge.wt))
