import math

def hashfunktion(namn):
    summa = 0
    for tkn in namn:
        summa = summa * 365 + ord(tkn)
    return summa % 7 + 1
# print(hashfunktion("oazrak"))

# Uppgift: Matchsticks


#funktion ger minstavärde med antal stickor
def minSiffra(numStickor, maxStickorEnSiffra, minStickorEnSiffra, stickLista):
    antalSiffror = math.ceil(numStickor/7) #Avrundar värdet upp för att få hur många siffror som krävs
    stickorKvar = numStickor
    resultmin = 0

    for i in range(0,antalSiffror):
        #För att få minsta antal stickor som kan användas per siffra används en max funktion som jämför minsta antal
        #stickor för en siffra (2) med antalet stickor kvar - (maxstickor*(antaletsiffror-1-i)), i är först 0 sen 1
        #sen två osv tills antalsiffror-1 uppkommer. vad som returneras är maxsiffran av dessa två, om de samma returneras
        #första siffran

        minStickorAttAnvanda = (max(minStickorEnSiffra, stickorKvar - maxStickorEnSiffra * (antalSiffror - 1 - i)))

        #Liknande till minStickorAttAnvanda sker exakt samma men för maxStickorAttAnvanda,
        # nu används en min funktion istället.
        maxStickorAttAnvanda = (min(maxStickorEnSiffra, stickorKvar - minStickorEnSiffra * (antalSiffror - 1 - i)))

        #Första siffran får ej börja med noll så en if-sats för att hindra resultatet från att aldrig hitta noll,
        # ex 168 skrivs ut istället för 108 för 15 stickor.
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

def maxSiffra(numStickor, maxStickorEnSiffra, minStickorEnSiffra, stickLista):
    #antal stickor dividerat med minsta antal stickor för en siffra, avrundas nedåt, math.floor hade kunnat använts här
    antalSiffror = numStickor // minStickorEnSiffra

    stickorKvar = numStickor
    resultmax = 0

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

def main():
    stickLista = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    maxStickorEnSiffra = 7
    minStickorEnSiffra = 2

    n = input()

    korListan = []
    for i in range(0,int(n)):
        numStickor = input()
        korListan.append(int(numStickor))

    for siffran in korListan:
        print(minSiffra(siffran, maxStickorEnSiffra, minStickorEnSiffra, stickLista),
              maxSiffra(siffran, maxStickorEnSiffra, minStickorEnSiffra, stickLista))

main()





