import random
from Graph import Vertex, Graph

class ArtistConnections:

    def __init__(self):
        self.vertList = Graph()
        # self.vertList = {}
        self.numVertices = 0
        self.nb0 = 0
        self.artist = 0
        self.repArt = 0
        self.repNb = 0

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """
    def list2str(self):
        for key in self.vertList:
            print(key)

    def load_graph(self, songLibaray):
        ## load the lines from the file

        with open(songLibaray, 'r') as file:
            lineArray = file.readlines()  # creating a new array with each song as 1 line, or 1 element of the array

            for line in lineArray:
                ### parse the songRecord and insert into the graph
                self.insertRecord(line) # Adding each song to the graph

        file.close()  # close open file

        self.vertList.setV() # This function sets the values in the graph

        return self.numVertices


    #This function inserts the record into the graph

    def insertRecord(self, record):
        # parse the string

        record = record[:len(record)-1]  # This line gets rid of the \n
        tokens = record.split(',')

        song = tokens[1]
        artist = tokens[2]
        neighbors = tokens[5].split(';')  # This is splitting each of the coArtists in the song

        # this for loop should create a vertex for each of the neighbors that are not already in the vertList
        for nB in neighbors:
            if nB in self.vertList:
                nB = self.vertList.getVertex(nB)
                # nB = self.vertList[nB]
            #     nB = self.vertList[nB] = Vertex(nB)
                nB.addNeighbor(artist)

                # nB.addSong(song)
                self.repNb += 1  # this should add 1 per repeated neighbor, for testing purposes
            else:  # if the coArtists doesn't exist already in the self.vertList, then add a new vertex
                nB = self.vertList.addVertex(nB)
                # nB = self.vertList[nB] = Vertex(nB)
                # nB = self.vertList[nB]
                nB.addNeighbor(artist)
                self.nb0 += 1  # this adds 1 per new new neighbor, or coArtist
                self.numVertices += 1
                # nB.addSong(song)


        # insert the record to graph

        # insert vertex for this artist

        if artist in self.vertList:  # this checks if the main artist already exists in the vertList
            currentVert = self.vertList.getVertex(artist)
            # currentVert = self.vertList[artist]

            self.repArt += 1  # this should add 1 for repeated main Artists, for testing purposes
        else:
            currentVert = self.vertList.addVertex(artist)
            # currentVert = self.vertList[artist] = Vertex(artist)
            self.artist += 1  # add 1 to the number of main artist.
            self.numVertices += 1

        ## insert info for this artist

        currentVert.addSong(song)  # Inserts song for the current Vertex
        for nb in neighbors:  # Adds each of the coArtists to the current vertex
            currentVert.addNeighbor(nb)
    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """
    def getVertices(self):
        result = 0
        for vertex in self.vertList:
            result += len(vertex.coArtists)
        return result

    def search_artist(self, artist_name):
        numSongs = len(self.vertList[artist_name].songs)
        artistLst = self.vertList[artist_name].getConnections()

        return numSongs, artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):
        two_hop_friends = []

        #
        # Write your code here
        #
        return two_hop_friends

    """
    Search the information of an artist based on the artist name

    """

    def recommend_new_collaborator(self, artist_name):
        artist = ""
        numSongs = 0

        #
        # Write your code here
        #

        return artist, numSongs

    """
    Search the information of an artist based on the artist name

    """

    def shortest_path(self, artist_name):
        path = {}

        #
        # Write your code here
        #
        return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    artistGraph = ArtistConnections()

    print(artistGraph.load_graph("TenKsongs_proj2"))
    # print("number of vertices: "+str(artistGraph.load_graph("TestingSongs")))
    print(artistGraph.search_artist("Mariah Carey"))
    print("number of edges is: " + str(artistGraph.getVertices()))
    # print(artistGraph.vertList.values())
    # print("number of main artists: " + str(artistGraph.artist))
    # print("number of repeated main artists : " + str(artistGraph.repArt))
    # print("number of neighbors: " + str(artistGraph.nb0))
    # print("number of repeated neighbors: " + str(artistGraph.repNb))
    # print("these are the keys: ")
    # for keys in artistGraph.vertList:
    #     print(keys)
    # print("neighbors for leon: " + str(artistGraph.vertList["Leon Lai"]))
