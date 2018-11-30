from Graph import Vertex

class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


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
            if nB in self.vertList.keys():
                nB = self.vertList[nB] # USING DICTIONARY
            else:  # if the coArtists doesn't exist already in the self.vertList, then add a new vertex
                nB = self.insertToGraph(nB)
                self.numVertices += 1
            nB.addNeighbor(artist) # Adds to the current nB's coArtists dictionary

        # insert the record to graph
        # insert vertex for this artist

        if artist in self.vertList.keys():  # this checks if the main artist already exists in the vertList
            currentVert = self.vertList[artist]
        else:
            currentVert = self.insertToGraph(artist)  # making a new artist vertex
            self.numVertices += 1

        ## insert info for this artist

        currentVert.addSong(song)  # Inserts song for the current Vertex

        for nb in neighbors:  # Adds each of the coArtists to the current vertex
            currentVert.addNeighbor(nb)

    # This method creates a new vertex for an artist only if the artist does not have a vertex yet, and returns the vertex
    def insertToGraph(self, artist):
        if artist not in self.vertList.keys():
            self.vertList[artist] = Vertex(artist)
        return self.vertList[artist]

    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    # Returns the number of edges in the graph, testing purposes
    def getEdges(self):
        result = 0
        for vertex in self.vertList:
            result += len(self.vertList[vertex].getConnections())
        return result
    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """
    def search_artist(self, artist_name):
        numSongs = len(self.vertList[artist_name].songs)
        artistLst = self.vertList[artist_name].getConnections()

        return numSongs, artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):
        two_hop_friends = []
        artist_name_Vertex = self.vertList[artist_name]
        artist_name_coArtists = artist_name_Vertex.getConnections()  # array with coArtists of the given artist

        for firstNb in artist_name_coArtists:  # Iterating through the array of coArtists of the given artist
            firstNbKeys = self.vertList[firstNb].getConnections()  # array with the coArtists of the current neigbor
            for secondNb in firstNbKeys:
                if secondNb == artist_name:  # If found the given artist just continue into the next iteration
                    continue
                # This is the condition that must be met in order for the artist to be added to the array
                # Basically if the secondNb's coArtist does not contain the given artist, and if not already in the
                # array, then add it.
                elif artist_name not in self.vertList[secondNb].coArtists and secondNb not in two_hop_friends:
                    two_hop_friends.append(secondNb)

        two_hop_friends.sort()  # sorts list before returning it
        return two_hop_friends

    """
    Search the information of an artist based on the artist name

    """
    # Checking for the weight of each of the edges in the graph, testing purposes
    def totalW(self):
        weight = 0
        for vertex in self.vertList.keys():
            weight += sum(self.vertList[vertex].coArtists.values())
        # this compares and returns the difference between the sum of all the edges and the "correct amount"
        return weight - 191394

    def recommend_new_collaborator(self, artist_name):
        artist = ""
        numSongs = 0
        artist_name_Vertex = self.vertList[artist_name]  # vertex of given artist
        artist_name_coArtists = artist_name_Vertex.getConnections()  # array of str
        possibleMatches = self.find_new_friends(artist_name)  # array of str
        # artist name => AA, AA => BB, return BB and artist name(w) + AA(w)

        for coArt in artist_name_coArtists:
            for nbOFnb in possibleMatches:
                if coArt in self.vertList[nbOFnb].coArtists:
                    weight = self.vertList[coArt].getWeight(nbOFnb) + \
                             + artist_name_Vertex.coArtists[coArt]
                    if weight >= numSongs:
                        artist = nbOFnb
                        numSongs = weight

        return artist, numSongs

    """
    Search the information of an artist based on the artist name

    """

    def shortest_path(self, artist_name):
        path = {}
        coveredArtists = list() # this list will keep track of the covered artists
        coveredArtists.append(artist_name) # Start with the given artist
        distance = 0
        done = False

        while not done:
            distance += 1
            temp = list(coveredArtists)  # creating a copy of coveredArtists
            for artist in temp:
                for coArt in self.vertList[artist].getConnections():
                    if coArt not in coveredArtists: # Check if the current nb is in coveredArtists
                        coveredArtists.append(coArt) # Add it to the list
                        path[coArt] = distance  # And to the dictionary as well
            if len(self.vertList.keys()) == len(coveredArtists): # Exit condition
                done = True

        return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    artistGraph = ArtistConnections()

    # print("number of vertices: " + str(artistGraph.load_graph("TenKsongs_proj2")))
    # print("number of vertices: "+str(artistGraph.load_graph("TestingSongs")))
    # print(artistGraph.search_artist("Mariah Carey"))
    # print("number of edges is: " + str(artistGraph.getEdges()))
    # print(artistGraph.vertList.values())
    # print("number of main artists: " + str(artistGraph.artist))
    # print("number of repeated main artists : " + str(artistGraph.repArt))
    # print("number of neighbors: " + str(artistGraph.nb0))
    # print("number of repeated neighbors: " + str(artistGraph.repNb))
    # print("artists involved in song: " + str(artistGraph.searchSong(""))) # Testing searchSong()
    # print(len(artistGraph.searchSong(""))) # Testing searchSong()
    # print("these are the keys: ")
    # for keys in artistGraph.vertList:
    #     print(keys)
    # print("neighbors for leon: " + str(artistGraph.vertList["Leon Lai"]))
    # y = artistGraph.find_new_friends("Mariah Carey") # Testing two hop friends
    # print("Two how neighbors: " + str(y)) # Testing two hop friends
    # print("Length of the two neighbor array: " +str(len(y))) # Testing two hop friends
    # print(artistGraph.vertList["Mariah Carey"])
    # print("Testing new collaborator using Mariah Carey, I should get Seal, 15")  # Testing new collaborator
    # print(artistGraph.recommend_new_collaborator("Mariah Carey"))  # Testing new collaborator
    # print("Difference in weights from the edges: " + str(artistGraph.totalW())) # Testing the total weight, should be 0
    # print("Testing shortest_path")
    # short_path = artistGraph.shortest_path('Mariah Carey')
    # # print(short_path) # Testing shortest_path
    # steps = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    # for value in short_path.values():
    #     steps[value] += 1
    #
    # print(steps)