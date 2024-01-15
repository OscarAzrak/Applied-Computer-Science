from PokemonClass import Pokemon
from hashtableClass2 import HashTable
import csv
hashtable = HashTable(1600)

def createPoke():
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
            hashtable.store(name, pokemon_ob)
    return hashtable
#def test():
createPoke()

hashtable.measure_distrbution()


print(len(hashtable))

#print(hashtable)

pokeNamn = input("Please enter the name of the pokemon: ")
print(hashtable[pokeNamn])


