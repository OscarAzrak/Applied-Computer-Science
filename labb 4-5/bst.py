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
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

gamla = Bintree()

startord = input()
slutord = input()



def makeChildren(startord):
    gamla.put(startord)
    for a in range(0,3):
        orde = list(startord)
        for bokstav in svealf:
            orde[a] = bokstav
            nytt = " ".join(orde)
            if nytt in svenska:
                if nytt not in gamla:
                    q.enqueue(nytt)
                    gamla.put(nytt)
                    if nytt == slutord:
                        print("hej")
                        return True
    #gör orden till en lista med tre element för varje bokstav
    #kollar om man ändrar första bokstaven till varje bokstav i alfabetet o kolla om det nya ordet finns i svenska
    #sen joina orden
    #

q = LinkedQ()
q.enqueue(startord)
variabel = False
while not q.isEmpty() and variabel is not True:
    node = q.dequeue
    print(node)
    variabel = makeChildren(node)
if variabel is not True:
    print("hejdå")


