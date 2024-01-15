import timeit
#This will take the code for which you want to measure the execution time. The default value is "pass".
#number: The stmt will execute as per the number is given here. The default value is 1000000.
#Where the timeit.timeit() function returns the number of seconds it took to execute the code.
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
        return self.artist < other



"""songlist = []


with open("unique_tracks.txt", "r", encoding = "utf-8") as songfile:
    for row in songfile:
        songrow = row.split("<SEP>")
        songs = Song(songrow[0],songrow[1],songrow[2],songrow[3] )
        songlist.append(songs)
print(songlist)"""


def readfile(filename):
    songlist = []
    with open(str(filename), "r", encoding="utf-8") as songfile:
        for row in songfile:
            songrow = row.split("<SEP>")
            songs = Song(songrow[0], songrow[1], songrow[2], songrow[3])
            songlist.append(songs)

    return songlist

"""def linsok(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1"""

def linsok(arr, x):
    for i, song in enumerate(arr):
        if x == song.artist:
            return i
    return -1


def binsok(arr, x):
    l = 0
    r = len(arr)-1

    while l <= r:
        m = (l+r)//2
        if arr[m].artist == x:
            return True
        else:
            if x < arr[m].artist:
                r = m - 1
            else:
                l = m + 1
    return False


"""def binsok(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)

        res = (x == arr[m])

        # Check if x is present at mid
        if (res == 0):
            return m - 1

        # If x greater, ignore left half
        if (res > 0):
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1

    return -1"""

#def hashsok(arr, x):


def main():
    filename = "unique_tracks.txt"
    lista = readfile(filename)
    mindreLista = lista[0:500000]
    n = len(mindreLista)
    print("Antal element =", n)

    forsta = lista[n-1]
    testartist = forsta.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(lista, testartist), number = 10000)
    print("binärsökningen tog", round(bintid, 4), "sekunder")

    #hashtid = timeit.timeit(stmt=lambda: hashsok(lista, testartist), number=10000)
    #print("binärsökningen tog", round(hashtid, 4), "sekunder")


main()