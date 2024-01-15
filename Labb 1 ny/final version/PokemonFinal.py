from PokemonClass import Pokemon
import csv
#Oscar Azrak , Hania Bakhsh
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


def search(pokeLista):
    pokeNamn = input("Please enter the name of the pokemon: ")
    for y in pokeLista:
        if y.name == pokeNamn:
            if True:
                poke1 = y
                print(poke1)
                return poke1


def search2(pokeLista):
    pokeNamn2 = input("\nEnter the name of the pokemon you want to compare: ")
    for y in pokeLista:
        if y.name == pokeNamn2:
            if True:
                poke2 = y
                print(y)
                return poke2


def comp(poke1, poke2):
    print(poke1 > poke2)
    print(poke1 < poke2)
    print(poke1 == poke2)


def main():
    test(pokeLista)
    poke1 = search(pokeLista)
    h = input("Do you want to compare " + poke1.name + " with another pokemon?(Yes/No)")
    if h == "Yes":
        poke2 = search2(pokeLista)
        comp(poke1,poke2)
    else:
        pass

main()