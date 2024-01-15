from bintreeFile import *
svenska = Bintree()
engelska = Bintree()
englista =[]

with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for radeng in engelskfil:
        for ordeng in radeng.split():
            engelska.put(ordeng)

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in engelska and svenska:
            print(ordet, end= " ")
        else:
            svenska.put(ordet)
print("\n")




"""for elem in svenska and engelska:

    if ord in engelska:
        if ord in engelska and svenska:
            englista.append(ord)"""

print(englista)


                #om nytt ord kolla om finns i svenska



#print(svenska)