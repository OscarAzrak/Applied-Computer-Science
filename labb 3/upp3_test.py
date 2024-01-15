from bintreeFile import Bintree
svenska = Bintree()
engelska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()     # Ett trebokstavsord per rad
        svenska.put(ordet)             # in i sökträdet

with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        for ord in rad.split():
            if ord in engelska:
                continue
            else:
                engelska.put(ord)
                if ord in svenska:
                    print(ord, end= " ")




