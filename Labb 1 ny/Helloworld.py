from PokemonClass import Pokemon
import csv

pokeLista = []
def createPoke(pokeLista):
    with open('pokemoninfo.csv','r') as infoFil:
        infoFilReader = csv.reader(infoFil)
        for row in infoFilReader:
            name = row[1]
            type1 = row[2]
            type2 = row[3]
            total = row[4]
            hp = row[5]
            attack = row[6]
            defense = row[7]
            sp_atk = row[8]
            sp_def = row[9]
            speed = row[10]
            gen = row[11]
            legendary = row[12]

            #skapar objekt
            pokemon_ob = Pokemon(name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary)
            pokeLista.append((pokemon_ob))
    return pokeLista
def test(pokeLista):
    createPoke(pokeLista)

    #print(pokeLista[2])
#def search2(pokeLista):
#    seek = input("Vad vill du söka på? \n Alternativ: namn, type1, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary")
#    pokeSearch = input()
#    for y in pokeLista:
#        if y.seek == pokeSearch:
#            print(pokeLista[y])


def search(pokeLista):
    global poke1, pokeNamn
    #x = input("söka på namn eller hp?")
    #if x == "namn":
    pokeNamn = input("namn på pokemon?")

    for y in pokeLista:
        if y.name == pokeNamn:
            if True:
                poke1 = y
                print(y)
                return poke1, pokeNamn






def search2(pokeLista):
    global poke2, pokeNamn2
    pokeNamn2 = input("namn på pokemon?")
    for y in pokeLista:
        if y.name == pokeNamn2:
            if True:
                poke2 = y
                print(y)
                return poke2, pokeNamn2

def comp(poke1, poke2, pokeNamn, pokeNamn2):
    if poke1.hp > poke2.hp:
        print(pokeNamn, "Har mer liv än ",pokeNamn2)
    elif poke1.hp < poke2.hp:
        print(pokeNamn, "har mindre hp än", pokeNamn2)
    elif poke1.hp == poke2.hp:
        print(pokeNamn, "har lika mycket liv som ", pokeNamn2)







    #elif x == "hp":
    #    pokeHp = input("hur mycket hp vill du söka på?")
    #    for a in pokeLista:
    #        if a.hp == pokeHp:
    #            if True:
    #                print(a)


    #print(pokeLista[])

test(pokeLista)
search(pokeLista)
search2(pokeLista)
#comp(poke1,poke2,pokeNamn, pokeNamn2)
