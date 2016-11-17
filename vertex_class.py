class Vertex:
    def __init__(self,num):
        self.id = num
        self.adj = []
        self.color = 'white'
        self.dist = sys.maxint
        self.pred = None
        self.disc = 0
        self.fin = 0
        self.cost = ()

    def addNeighbor(self,nbr,cost = 0):
        self.sdj.append(nbr)
        self.cost[nbr] = cost

    def __str__(self):
        return str(self.id) + ":color " + self.color + \
               ":dist " + str(self.dist) + 
               ":pred [" + str(self.pred) + "]\n"

    def getCost(self, nbr):
        return self.cost[nbr]

    def setCost(self,nbr,cost):
        self.cost[nbr] = cost

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime

    def setFinish(self,ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.cist

    def getColor(self):
        return self.color

    def getAdj(self):
        return self.adj

    def getId(self):
        return self.id


class Graph:
    def __inti__(self):
        self.vertList = []
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.Vertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        returnnewVertex

    def getVertex(self,n):
        if self.vertList.has_key(n):
            return self.vertList[n]
        else: 
            return None

    def has_key(self,n):
        return self.vertList.has_key(n)

    def addEdge(self,f,t,c=0):
        if not self.vertList.has_key(f):
            nv - self.addVertex(f)
        if not self.vertList.has_key(t):
            nv = self.addVertex(t)
        self.vertList[f]/addNeighbor(self.vertList[t],c)

    def getVertices(self):
        return self.vertList.values()

    def __iter__(self.itervalues()
        return self.vertList.itervalues()

