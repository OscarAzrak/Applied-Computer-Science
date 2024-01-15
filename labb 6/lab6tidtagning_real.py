import timeit
#stmtm:This will take the code for which you want to measure the execution time. The default value is "pass".
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
        return self.artist < other.artist






def readfile(filename):
    songlist = []
    with open(str(filename), "r", encoding="utf-8") as songfile:
        for row in songfile:
            songrow = row.split("<SEP>")
            songs = Song(songrow[0], songrow[1], songrow[2], songrow[3])
            songlist.append(songs)

    return songlist



#O(n)
#Inspirerad av föreläsning
def linsok(arr, x):
    for i in arr:
        if x == i.artist:
            return i
    return -1


#O(log(n))
#Inspirerad av GeeksforGeeks
def binsok(arr, x):
    f = 0
    l = len(arr)
    while f <= l:
        m = f + (l - f) // 2


        res = arr[m].artist

        # Check if x is present at mid
        if res == x:
            return m

        # If x greater, ignore left half
        elif res < x:
            f = m + 1
        # If x is smaller, ignore right half
        else:
            l = m - 1
    return -1


def insert(arr):
    arr_dict ={}
    for i in arr:
        arr_dict[i.artist] = i
    return arr_dict



#O(1)
def hashsok(arr_dict, x):
    while arr_dict[x]:
        return True
    else:
        return False



def main():
    filename = "unique_tracks.txt"
    lista = readfile(filename)
    mindreLista = lista[0:1000000]
    n = len(mindreLista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt=lambda: linsok(mindreLista, testartist), number=10000)
    print("Linjärsökningen tog", round(linjtid, 5) , "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(mindreLista, testartist), number=10000)
    print("binärsökningen tog", round(bintid, 5), "sekunder")

    arr_dict = insert(mindreLista)

    hashtid = timeit.timeit(stmt=lambda: hashsok(arr_dict, testartist), number=10000)
    print("hashsökningen tog", round(hashtid, 5), "sekunder")


#                    n = 250 000	 n = 500 000	    n = 1 000 000
#Linjärsökning	        39.32143 	  1.87751	            0.33795
#Binärsökning	        0.04179	      0.04302	            0.04438
#Sökning i hashtabell	0.0023	      0.00255	            0.00277

main()
