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



songlist = []


with open("unique_tracks.txt", "r", encoding = "utf-8") as songfile:
    for row in songfile:
        songrow = row.split("<SEP>")
        songs = Song(songrow[0],songrow[1],songrow[2],songrow[3] )
        songlist.append(songs)
print(songlist)


def readfile(filename):
    with open(str(filename), "r", encoding="utf-8") as songfile:
        for row in songfile:
            songrow = row.split("<SEP>")
            songs = Song(songrow[0], songrow[1], songrow[2], songrow[3])
            songlist.append(songs)

    return songlist

def main():
    filename = "unique_tracks.txt"
    lista = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")