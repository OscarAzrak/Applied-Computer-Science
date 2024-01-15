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
        songs = Song(songrow[0],songrow[1],songrow[2],songrow[3])
        songlist.append(songs)
print(songlist)