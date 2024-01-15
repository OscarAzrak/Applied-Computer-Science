import math

def hashfunktion(namn):
    summa = 0
    for tkn in namn:
        summa = summa * 365 + ord(tkn)
    return summa % 7 + 1
# print(hashfunktion("oazrak"))

# Uppgift: Matchsticks


#funktion ger minstavärde med antal stickor
def minTal(numStickor, maxStickorEnSiffra, minStickorEnSiffra, stickLista):
    antalSiffror = math.ceil(numStickor/maxStickorEnSiffra) #Avrundar värdet upp för att få hur många siffror som krävs
    stickorKvar = numStickor
    resultmin = 0

    for i in range(0,antalSiffror):
        #max-funktion används för att jämföra vilken siffra som e störst mellan minStickorEnSiffra eller antalet stickor
        #som är kvar minus maxstickor gånger antalsiffror-1, x - 7(x-1) sedan subtraheras även i för varje gång
        minStickorAttAnvanda = (max(minStickorEnSiffra, stickorKvar - maxStickorEnSiffra * (antalSiffror - 1 - i)))

        #Liknande till minStickorAttAnvanda sker exakt samma men för maxStickorAttAnvanda,
        #nu används en min funktion istället och minStickorEnSiffra, 2
        maxStickorAttAnvanda = (min(maxStickorEnSiffra, stickorKvar - minStickorEnSiffra * (antalSiffror - 1 - i)))

        #Första siffran får ej börja med noll så en if-sats för att hindra resultatet från att aldrig hitta noll,
        #annars skrivs ex 168 ut istället för 108 för 15 stickor.
        if resultmin == 0:
            for index in range(1, 10):
                if minStickorAttAnvanda <= stickLista[index] <= maxStickorAttAnvanda:
                    #resultatet mult. med 10 för att kunna addera rätt, alternativt hade det funkat att addera som strings
                    resultmin = resultmin * 10 + index
                    #Antal stickor som är kvar subtraheras med den motsvarande siffran till index,
                    #så om index=0 subtraheras 6
                    stickorKvar -= stickLista[index]
                    break
        else:
            for index in range(0, 10):
                if minStickorAttAnvanda <= stickLista[index] <= maxStickorAttAnvanda:
                    resultmin = resultmin * 10 + index
                    stickorKvar -= stickLista[index]
                    break
    return resultmin


#Returnerar högsta siffran med numStickor st tändstickor
def maxTal(numStickor, maxStickorEnSiffra, minStickorEnSiffra, stickLista):
    #antal stickor dividerat med minsta antal stickor för en siffra, avrundas nedåt, math.floor hade kunnat använts här
    #för att få hur många siffror som ska användas
    antalSiffror = numStickor // minStickorEnSiffra

    stickorKvar = numStickor
    resultmax = 0
    #for-loop antalSiffror gånger för att hitta det största värde per siffra som sedan läggs ihop som resultatmax
    for i in range(0, antalSiffror):
        minStickorAttAnvanda = (max(minStickorEnSiffra, stickorKvar - maxStickorEnSiffra * (antalSiffror - 1 - i)))
        maxStickorAttAnvanda = (min(maxStickorEnSiffra, stickorKvar - minStickorEnSiffra * (antalSiffror - 1 - i)))
        if resultmax == 0:
            #kollar sticklistan från slutet till början för att nu bör den högsta siffran vara i början och ej i slutet
            for index in range(9, 0, -1):
                if minStickorAttAnvanda <= stickLista[index] <= maxStickorAttAnvanda:
                    resultmax = resultmax * 10 + index
                    stickorKvar -= stickLista[index]
                    break
        else:
            for index in range(0,10):
                if minStickorAttAnvanda <= stickLista[index] <= maxStickorAttAnvanda:
                    resultmax = resultmax * 10 + index
                    stickorKvar -= stickLista[index]
                    break
    return resultmax


#kollar om antal rader n input är korrekt
def checknFTOK(n): #function that checks wether the size of the board is correct
    nOK = False
    try:
        n = int(n)
        if n > 0:
            nOK = True
        else:
            pass
    except ValueError:
        pass
    return nOK


#undersöker om inputs är korrekt.
def checkNumStickorOK(numStickor):
    numStickorOK = False
    try:
        numStickor = (numStickor)
        if 2 <= int(numStickor) <= 100:
            numStickorOK = True
        else:
            pass
    except ValueError:
        pass
    return numStickorOK

#tar emot input från användaren och undersöker om det är korrekt
def numSticks():
    numStickorOK = False
    while numStickorOK == False:
        numStickor = input()
        numStickorOK = checkNumStickorOK(numStickor)
    return numStickor

def main():
    # antal stickor som behövs från 0-9, första siffran är hur många stickor siffran 0 behöver


    #lista med antalet stickor per index, index 0 kräver 6 stickor, osv
    stickLista = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    # största talet i listan
    maxStickorEnSiffra = max(stickLista)
    # minsta talet i listan
    minStickorEnSiffra = min(stickLista)

    #kollar om antal rader man ger i input är rätt, måste vara över noll och en siffra
    nOK = False
    while nOK == False:
        n = input()
        nOK = checknFTOK(n)

    #korListan sparar vilka indata som ska undersökas
    korListan = []

    #for-loop som går igenom inputet n antal gånger från första input värdet, kollar även med hjälp av
    #numSticks() funktionen om input är korrekt

    #loopar igenom n gånger för att få inputsen, kollar även om inputsen är rätt. lägger till inputsen i korListan
    for i in range(0,int(n)):
        numStickor = numSticks()
        korListan.append(int(numStickor))

    #for-loop som printar resultat för varje input, minsta värde respektive största värdet.
    for siffran in korListan:
        print(minTal(siffran, maxStickorEnSiffra, minStickorEnSiffra, stickLista),
              maxTal(siffran, maxStickorEnSiffra, minStickorEnSiffra, stickLista))

main()





