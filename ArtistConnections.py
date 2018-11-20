import random
from P2.Graph import Vertex

class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """

    def load_graph(self, songLibaray):
        ## load the lines from the file

        with open(songLibaray, 'r') as file:
            lineArray = file.readlines() # creating a new array with each song as 1 line, or 1 element of the array

            for line in lineArray:
                ### parse the songRecord and insert into the graph
                self.insertRecord(line) # Adding each song to the graph

        file.close()  # close open file

        return self.numVertices


    #This function inserts the record into the graph

    def insertRecord(self, record):
        # parse the string

        record = record[:len(record)-1]  # This line gets rid of the \n
        tokens = record.split(',')

        song = tokens[1]
        artist = tokens[2]
        neighbors = tokens[5].split(';')  # This is splitting each of the artists in the song

        # insert the record to graph

        # insert vertex for this artist

        if artist in self.vertList:
            currentVert = self.vertList[artist]
        else:
            currentVert = self.vertList[artist] = (Vertex(artist))
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

    def search_artist(self, artist_name):
        numSongs = len(self.vertList[artist_name].songs);
        artistLst = self.vertList[artist_name].getConnections

        # for key in [self.vertList[artist_name].coArtists]:
        #     artistLst.append(key)

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

    # print(artistGraph.load_graph("TenKsongs_proj2"))
    print(artistGraph.load_graph("TestingSongs"))
    print(artistGraph.search_artist("Mariah Carey"))
