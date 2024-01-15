import hashlib
import timeit

#tiden att hasha 100 000 ord, siffror, och random, så som låtlistan

#antal kollisioner
#Hur påverkar kollisionerna om några tecken i strängen ändras



def readfile(filename):
    listan = []
    with open(str(filename), "r", encoding="utf-8") as file:
        for row in file:
            listan.append(row)
    return listan

def readfile3(filename):
    listan = []
    with open(str(filename), "r", encoding="utf-8") as file:
        for row in file:
            row = row.replace("TR", "")
            row = row.replace("SO", "")
            row = row.replace("\n", "")
            row = row.replace("12", "")
            row = row.replace("<SEP>", "")
            listan.append(row)
    return listan

def sha1(row):
    s = hashlib.sha1(str.encode(row)).hexdigest()
    return s

def tatidsha1(listan):
    for row in listan:
        sha1(row)

def shacount(listan):
    shadic = {}
    count = 0
    for row in listan:
        keyvalue = sha1(row)
        if keyvalue in shadic:
            count += 1
        else:
            shadic[keyvalue] = row
    return count

def hashfunction(row,n):
    h = ''
    for elem in row:
        val = ord(elem)
        h = h + str(val)
    return int(h) % n

def tatidhash(listan,n):
    for row in listan:
        hashfunction(row,n)

def hashcount(listan,n):
    hashdic = {}
    count = 0
    for row in listan:
        keyvalue = hashfunction(row,n)
        if keyvalue in hashdic:
            count += 1
        else:
            hashdic[keyvalue] = row
    return count

def main():
    x = 50
    songfilename = "unique_tracks.txt"
    lista = readfile(songfilename)
    mindreListasong = lista[0:1000000]
    nSL = 1000003
    print("Antal element =", nSL)

    sha1tidSL = timeit.timeit(lambda: tatidsha1(mindreListasong), number=1)
    print("Sha1 tog", round(sha1tidSL, 5), "sekunder")
    hashtidSL = timeit.timeit(lambda: tatidhash(mindreListasong,nSL), number=1)
    print("hashfunktionen tog", round(hashtidSL, 5), "sekunder")

    print("Antal kollisioner för",nSL, "st låtdata:")
    print("SHA-1 kollisioner:",shacount(mindreListasong))
    print("Min hashfunktions kollisioner:",hashcount(mindreListasong,nSL), "hashcount")

    print("-"*x)

    numberlistfilename = "numlist.txt"
    numlist = readfile(numberlistfilename)
    nNL = len(numlist)
    print("Antal element =", nNL)

    sha1tidNL = timeit.timeit(lambda: tatidsha1(numlist), number=1)
    print("Sha1 tog", round(sha1tidNL, 5), "sekunder")
    hashtidNL = timeit.timeit(lambda: tatidhash(numlist, nNL), number=1)
    print("hashfunktionen tog", round(hashtidNL, 5), "sekunder")

    print("Antal kollisioner för", nNL, "st nummer:")
    print("SHA-1 kollisioner:", shacount(numlist))
    print("Min hashfunktions kollisioner:", hashcount(numlist, nNL), "hashcount")

    print("-"*x)

    alphafilename = "engelskaord.txt"
    alphalista = readfile(alphafilename)
    nAL = len(alphalista)
    print("Antal element =", nAL)

    sha1tidAL = timeit.timeit(lambda: tatidsha1(alphalista), number=1)
    print("Sha1 tog", round(sha1tidAL, 5), "sekunder")
    hashtidAL = timeit.timeit(lambda: tatidhash(alphalista, nAL), number=1)
    print("hashfunktionen tog", round(hashtidAL, 5), "sekunder")

    print("Antal kollisioner för", nSL, "st engelska ord:")
    print("SHA-1 kollisioner:", shacount(alphalista))
    print("Min hashfunktions kollisioner:", hashcount(alphalista, nAL), "hashcount")

    print("-"*x)

    songfilename2 = "unique_tracks.txt"
    songlista2 = readfile3(songfilename2)
    mindreListasong2 = songlista2[0:370099]
    nSL2 = len(mindreListasong2)
    print("Antal element =", nSL2)

    sha1tidSL2 = timeit.timeit(lambda: tatidsha1(mindreListasong2), number=1)
    print("Sha1 tog", round(sha1tidSL2, 5), "sekunder")
    hashtidSL2 = timeit.timeit(lambda: tatidhash(mindreListasong2, nSL2), number=1)
    print("hashfunktionen tog", round(hashtidSL2, 5), "sekunder")

    print("Antal kollisioner för", nSL2, "st låtdata:")
    print("SHA-1 kollisioner:", shacount(mindreListasong2))
    print("Min hashfunktions kollisioner:", hashcount(mindreListasong2, nSL2), "hashcount")


main()


