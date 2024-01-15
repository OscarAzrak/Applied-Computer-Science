from bintreeFile import *
from linkedQFile import LinkedQ
import string

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


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

parent = ParentNode(startord)

q = LinkedQ

def writeChain(slutordsnod):
    while slutordsnod:
        print(slutordsnod.word)
        slutordsnod = slutordsnod.parent


def makeChildren(parent,q):
    gamla.put(parent)
    #för varje bokstav i alfabetet ska den först byta ut första tills den hittar ett ord,
    for i in range(0,3):
        orda = list(parent)
        for bokstav in svealf:
            orda[i] = bokstav
            nyttord = "".join(orda)
            if nyttord in svenska:
                if nyttord not in gamla:
                    q.enqueue(nyttord)
                    gamla.put(parent.nyttord)



while not q.isEmpty:
    nod = q.dequeue
    makeChildren(nod, q)
else:
    writeChain(parent)
    print("Det finns en väg till",slutord)

