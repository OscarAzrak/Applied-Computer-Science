from bintreeFile import *
from linkedQFile import LinkedQ
import string

svealf = list(string.ascii_lowercase)
svextr = ["å", "ä", "ö"]

for bokst in svextr:
    svealf.append(bokst)

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        svenska.put(ordet)

gamla = Bintree()

startord = input()
slutord = input()

ordlista = []
def makeChildren(startord):
    gamla.put(startord)
    #för varje bokstav i alfabetet ska den först byta ut första tills den hittar ett ord,
    for i in range(0,3):
        orda = list(startord)
        for bokstav in svealf:
            orda[i] = bokstav
            nyttord = "".join(orda)
            if nyttord in svenska:
                if nyttord not in gamla:
                    print(nyttord)
                    ordlista.append(nyttord)
                    gamla.put(nyttord)

    print(ordlista[-1])




ordee = makeChildren(startord)
#print(ordee)


