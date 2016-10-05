#Implementing adjacency list in Python.
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self,nbr,weight):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        return None

    def __contains__(self,n):
        return n in self.vertexList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertexList:
            nv = addVertex(f)
        if t not in self.vertexList:
            nv = addVertex(t)
        self.vertexList[f].addNeighbour(self.vertexList[t],cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)
print g.getVertices()
print g.vertexList

