from bintreeFile import*
from linkedQFile import LinkedQ
import string
import sys



class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


def makeChildren(nod, svenska, alfabet,gamla,q):
    väg = [nod]
    for i in range(0,3):
        orda = list(nod.word)
        for bokstav in alfabet:
            orda[i] = bokstav
            nyttord = "".join(orda)
            if nyttord in svenska:
                väg.append(ParentNode(nyttord, nod))
                if nyttord not in gamla:
                    x = ParentNode(nyttord,nod)
                    q.enqueue(x)
                    gamla.put(nyttord)
    return väg


def writechain(slutordsnod):
    väg = [slutordsnod.word]
    if slutordsnod.parent:
        väg = writechain(slutordsnod.parent) + väg
    return väg

def main():
    svealf = list(string.ascii_lowercase)
    sveextr = ["å", "ä", "ö"]
    for bokst in sveextr:
        svealf.append(bokst)
    svenska = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            svenska.put(ordet)

    gamla = Bintree()

    startord = input("startord: ")
    slutord = input("slutord: ")
    q = LinkedQ()

    ab = ParentNode(startord)
    q.enqueue(ab)

    while not q.isEmpty():
        nod = q.dequeue()
        nyChild = makeChildren(nod, svenska, svealf, gamla, q)

        for nodes in nyChild:

            if nodes.word == slutord:
                p = "Det finns en väg till " + slutord + " "
                p = p + "vilket är: " + " ".join(writechain(nodes))
                print(p)
                sys.exit()
    print("Det finns ingen väg till ordet", slutord)






main()