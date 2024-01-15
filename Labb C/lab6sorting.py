import timeit
#This will take the code for which you want to measure the execution time. The default value is "pass".
#number: The stmt will execute as per the number is given here. The default value is 1000000.
#Where the timeit.timeit() function returns the number of seconds it took to execute the code.

#Oscar Azrak
#Hania Bakhsh

class Song():
    def __init__(self, trackid, songid, artist, songname):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.songname = songname


    def __str__(self):
        return str(self.trackid) +" "+ str(self.songid) + " "+ str(self.artist) +" "+  str(self.songname)

    __repr__ = __str__

    def __lt__(self, other):
        if isinstance(other, Song):
            if self.artist != other.artist:
                return self.artist.lower() < other.artist.lower()
            else:
                return self.songname.lower() < other.songname.lower()




#O(n^2)
#inspirerad av kurslitteratur
def bubbleSort(list_1):
    for passnum in range(len(list_1) - 1, 0, -1):
        for i in range(passnum):
            if list_1[i].artist > list_1[i + 1].artist:
                temp = list_1[i].artist
                list_1[i].artist = list_1[i + 1].artist
                list_1[i + 1].artist = temp


#Inspireade av föreläsning
#Ω(n log(n))
def quicksort(list_1):
    sista = len(list_1) - 1
    qsort(list_1, 0, sista)


def qsort(list_1, low, high):
    pivotindex = (low + high) // 2
    # flytta pivot till kanten
    list_1[pivotindex].artist, list_1[high].artist = list_1[high].artist, list_1[pivotindex].artist

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(list_1, low - 1, high, list_1[high].artist)

    # flytta tillbaka pivot
    list_1[pivotmid].artist, list_1[high].artist = list_1[high].artist, list_1[pivotmid].artist

    if pivotmid - low > 1:
        qsort(list_1, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(list_1, pivotmid + 1, high)


def partitionera(list_1, v, h, pivot):
    while True:
        v = v + 1
        while list_1[v].artist < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and list_1[h].artist > pivot:
            h = h - 1
        list_1[v].artist, list_1[h].artist = list_1[h].artist, list_1[v].artist
        if v >= h:
            break
    list_1[v].artist, list_1[h].artist = list_1[h].artist, list_1[v].artist
    return v





def readfile(filename):
    songlist = []
    with open(str(filename), "r", encoding="utf-8") as songfile:
        for row in songfile:
            songrow = row.split("<SEP>")
            songs = Song(songrow[0], songrow[1], songrow[2], songrow[3])
            songlist.append(songs)

    return songlist




def main():
    filename = "unique_tracks.txt"
    lista = readfile(filename)
    mindreLista = lista[0:1000]
    n = len(mindreLista)
    print("Antal element =", n)

    #forsta = lista[n-1]
    #testartist = forsta.artist


    bubbletid = timeit.timeit(stmt=lambda: bubbleSort(mindreLista), number=10)
    print("Bubble sorteringen tog", round(bubbletid, 4), "sekunder")

    quicksortering = timeit.timeit(stmt=lambda: quicksort(mindreLista), number=10)
    print("Quicksorteringen tog", round(quicksortering, 4), "sekunder")


#   n	                1000	10 000	    100 000	    1 000 000
#   bubbelsortering	   0.8789	96.7813
#   quicksort	       0.0176	0.2221	    3.2251 	    51.3949
main()