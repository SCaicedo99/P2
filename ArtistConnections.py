import random
from Graph import Vertex, Graph

class ArtistConnections:

    def __init__(self):
        self.vertList = {}
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
                nB = self.vertList[nB] # USING DICTIONARY
                self.repNb += 1  # this should add 1 per repeated neighbor, for testing purposes

            else:  # if the coArtists doesn't exist already in the self.vertList, then add a new vertex
                nB = self.insertToGraph(nB)
                self.nb0 += 1  # this adds 1 per new new neighbor, or coArtist
                self.numVertices += 1

            # nB.addSong(song) # TODO COMMENT THIS OUT BEFORE SUBMITTING
            nB.addNeighbor(artist)


        # insert the record to graph

        # insert vertex for this artist

        if artist in self.vertList:  # this checks if the main artist already exists in the vertList
            currentVert = self.vertList[artist]

            self.repArt += 1  # this should add 1 for repeated main Artists, for testing purposes
        else:
            currentVert = self.insertToGraph(artist) # making a new artist vertex
            self.artist += 1  # add 1 to the number of main artist.
            self.numVertices += 1

        ## insert info for this artist

        currentVert.addSong(song)  # Inserts song for the current Vertex

        for nb in neighbors:  # Adds each of the coArtists to the current vertex
            currentVert.addNeighbor(nb)

    def insertToGraph(self, artist): # This method creates a new vertex for an artist only if the artist does not have a vertex yet, and returns the vertex
        if artist not in self.vertList:
            self.vertList[artist] = Vertex(artist)
        return self.vertList[artist]

    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    def searchSong(self, item):  # this method given a song will return all the artists involved, just for testing purposes
        result = []
        for artist in self.vertList:
            for song in self.vertList[artist].songs:
                if song == item:
                    result.append(artist)

        return result

    def getVertices(self):
        result = 0
        for vertex in self.vertList:
            result += len(self.vertList[vertex].coArtists)
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
        artist_name_coArtists = artist_name_Vertex.coArtists.keys() # array with coArtists of the given artist
        iterfor1 = 0
        iterfor2 = 0
        iterfor3 = 0
        # for coArtists in artist_name_coArtists: # This line iterates through all the coArtists in artist_name Vertex
        #     iterfor1 += 1
        #     currCoArtist = self.vertList[coArtists].coArtists.keys() # Current coArtist vertex
        #     for nb in currCoArtist: # This iterates through the neighbors of the current coArtist
        #         iterfor2 += 1
        #         nbVertex_Keys = self.vertList[nb].coArtists.keys()
        #         if nb != artist_name:
        #             for nbOFnb in nbVertex_Keys: # This iterates through the neighbors of the neighbors of current coArtist
        #                 iterfor3 += 1
        #                 if artist_name not in self.vertList[nbOFnb].coArtists and nbOFnb not in two_hop_friends:
        #                     two_hop_friends.append(nbOFnb)
        for firstNb in artist_name_coArtists:
            firstNbKeys = self.vertList[firstNb].coArtists.keys()
            for secondNb in firstNbKeys:
                secondNbKeys = self.vertList[secondNb].coArtists.keys()
                for friends in secondNbKeys:
                    if friends not in artist_name_coArtists and artist_name not in self.vertList[friends].coArtists.keys() and friends != artist_name:
                        two_hop_friends.append(friends)
        two_hop_friends.sort() # sorts list before returning it
        print("first loop " + str(iterfor1))
        print("second loop " + str(iterfor2))
        print("third  loop " + str(iterfor3))

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

    print("number of vertices: " + str(artistGraph.load_graph("TenKsongs_proj2")))
    # print("number of vertices: "+str(artistGraph.load_graph("TestingSongs")))
    # print(artistGraph.search_artist("Mariah Carey"))
    # print("number of edges is: " + str(artistGraph.getVertices()))
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
    y = artistGraph.find_new_friends("Mariah Carey")
    print("Two how neighbors: " + str(y))
    print("Length of the two neighbor array: " +str(len(y)))
    print(artistGraph.vertList["Mariah Carey"])
    correct = ['A Tundra', 'Aaron Watson', 'Aftermath', 'Al Duvall', 'Alex', 'Alfredo Guti\xc3\xa9rrez', 'Alkonost', 'Angels', 'Arthur Brown', 'Asterisk*', 'Atman', 'Azukx', 'Becky Baeling', 'Beenie Man', 'Birdapres', 'Bitter End', 'Bobby Darin', 'Bobby Hutcherson', 'Bounty Killer', 'Brian Littrell', 'Busdriver', 'C.L. Smooth', 'Circle Jerks', 'Claire Hamill', 'Commander Cody And His Lost Planet Airman', 'Criminal Class USA is Hush Hush Revolution', 'Curtis', "D'Molls", 'DJ Dips', 'DJ Phiene', 'Dale Hawkins', 'Deathstar', 'Deep Blue Something', 'Del Tha Funkee Homosapien', 'Don Davis', 'Double Image', 'Eastmountainsouth', 'Edgar Bori', 'Eno', 'Enrique Iglesias', 'Equilibrium', 'Erick Sermon', 'Eyes Cream', 'Fake Problems', 'Fortitude', 'Foxy Brown', 'Frank Ifield', 'GG Allin', 'Hassan Annouri feat. Cassandra Steen', 'Ice', 'JC Lodge', 'Jaguares', 'Jeff & Sheri Easter', 'Jenney', 'Joe Heaney', 'Jorge Alfano', 'Jo\xc3\xa3o Gilberto', 'Justin', 'KT Tunstall', 'Kardinal Offishall / Keri Hilson', 'Kati', 'La Charanga Rubalcaba', 'La Divina Pastora', 'Len Barry', 'Les Rythmes Digitales feat. Nik Kershaw', 'Less Than Jake', 'Lily Allen Featuring Ours', 'Livingston Taylor', 'Malefaction', 'Mance Lipscomb', 'Maria Callas/Gianni Raimondi/Gabriella Carturan/Plinio Clabassi/Nicola Rossi-Lemeni/Coro del Teatro alla Scala_ Milano/Noberto Mola/Orchestra del Teatro alla Scala_ Milano/Gianandrea Gavazzeni', 'Markus', 'Marty Robbins', 'Matisyahu', 'Michael English', 'Michael McDonald', 'Mick Clarke', 'Migraine', "Mike Jones (Featuring CJ_ Mello & Lil' Bran)", 'Mindless Self Indulgence', 'Monster Magnet', 'Monty Are I', 'Mudhoney', 'Mystic Revelation of Rastafari', 'Norman Howard', 'Obie Bermudez', 'Olive', 'Out Of The Grey', 'Pelt', 'Peret', 'Poptart Monkeys', 'Pyranja', 'Ricky Martin Feat. La Mari de "Chambao', 'Ruffneck', 'RyanDan', 'SUMO', 'Samba Mapangala and Orchestra Virunga', 'Seal', 'Sergio Dalma', 'Shakira Featuring Wyclef Jean', 'Skeeter Davis', 'Solistiyhtye Suomi', 'Spunk', 'State of Chaos', 'Strata', 'Sukhbir', 'Super700', 'The Black Crowes', 'The Clark Sisters', 'The Doors', 'The Frantic', 'The Knightsbridge Strings', 'The London Pops Orchestra', 'The Monroes', 'The Nightraver & The Magican', 'The Panic Channel', 'The Sex Pistols', 'The Token', 'Tito Puent\xc3\xa9', 'Tom Collier', 'Tranzas', 'Trick Trick / Obie Trice', 'Tum Tum / Double T / LiL Ronnie', 'Uman', 'Urge Overkill', 'Wilshire', 'Winifred Phillips', 'YZ']
    print("The right # of neigbor should be: " +str(len(correct)))
