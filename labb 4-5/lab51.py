from bintreeFile import*
from linkedQFile import LinkedQ
import string
import sys



class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def __str__(self):
        return str(self.word)

"""class SolutionFound(Exception):
    pass"""



def makeChildren(ab, q, gamla, svealf, svenska):
    #q.enqueue(ab)
    #gamla.put(ab.word)
    #print(gamla)
    #q.enqueue(ab.word)
    väg = [ab]
    for i in range(0,3):
        orda = list(ab.word)
        #print(orda)
        for bokstav in svealf:
            orda[i] = bokstav
            nyttord = "".join(orda)
            #print(nyttord)
            if nyttord in svenska:
                if nyttord not in gamla:
                    x = ParentNode(nyttord,ab)
                    q.enqueue(x)
                    gamla.put(nyttord)
                    #ab = x
                    ab = ParentNode(nyttord, ab)
                    #print(q)
                    #gamla.put(parent.nyttord)
                    #writechain(nyttord)


def writechain(slutordsnod):
    #print("IM HERE       AAAAAA")
    while slutordsnod.parent:
        print(slutordsnod.parent)
        slutordsnod = slutordsnod.parent
        writechain(slutordsnod)
        #print("aaaaaaaaaaaaa")
        break

    #print("hejdååååå")



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
        # print("yes")
        nod = q.dequeue()
        makeChildren(nod, q, gamla, svealf, svenska)

        # print(nod.word)
        if nod.word == slutord:
            print("Det finns en väg till ", slutord)
            #print(nod.word)
            writechain(nod)
            sys.exit()

        #if
        else:
            makeChildren(nod, q, gamla, svealf, svenska)


main()