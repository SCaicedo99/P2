class Vertex:
    def __init__(self, artist):
        self.id = artist
        self.songs = [] # songs the artists wrote, or was part of
        self.coArtists = {}  # the coArtists are going to be stored in a array

    # Adds song to the vertex array's of songs
    def addSong(self, song):
        self.songs.append(song)

    # Adds the coArtists of the vertex
    def addNeighbor(self, nbr):
         if nbr != self.getId():  # Checking if the nb to be added is the vertex, ignore it if it is
            if nbr in self.coArtists:
                self.coArtists[nbr] += 1
            else:
                self.coArtists[nbr] = 1

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in self.coArtists])

    def getConnections(self):
        return self.coArtists.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.coArtists[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __getitem__(self, item):
        return self.getVertex(item)

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    g = Graph()
    for i in range(5):
        g.addVertex(i)

    g.addEdge(1,2,1)
    g.addEdge(1,5,2)
    g.addEdge(2,5,3)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
