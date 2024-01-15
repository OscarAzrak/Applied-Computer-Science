class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary):
        self.namn = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.gen = gen
        self.legendary = legendary

    def __str__(self):
        rep = "Pokemon\n"
        rep += "name: " + self.name + "\n"  + "type1: " + self.type1 + "\n"  + "type2: " + self.type2 + "\n" + "total: " + self.total + "\n" + "hp: " + self.hp + "\n" + "attack: " + self.attack + "\n" + "defense" + self.defense + "\n" + "sp_atk: " + self.sp_atk + "\n" + "sp_def: " + self.sp_def + "\n" + "speed: " + self.speed + "\n" + "gen: " + self.gen + "\n" + "legendary: " + self.legendary + "\n"
        return rep

    #


  #def__lt__(self, )



  #def4


  #def5

#print()
poke_list = []


#main()
#print(poke_list)

#söker efter en pokemon i listan
def search(pokeList):
    x = input("Vad vill du söka på? \n Alternativ: namn, type1, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary")
    pokeNamn = input()
    for y in pokeList:
        if y.x == pokeNamn:
            print(pokeList[y])
    #elif x == "hp":
    #    pokeHp = input("hur mycket hp vill du söka på?")
    #    for a in pokeList:
    #        if a.hp == hp:
    #            print(pokeList[a])
    #    else:
    #        continue
        #find(x)
    #print(x)
def main():
    poke_list = []
    #import re

  #läser in alla rader från filen
    #filnamn = "pokemon.csv"
    with open("pokemoninfo.csv.webarchive", "r") as file:
        for attri in file.readlines():
            pattern = attri.split(",")
            #pattern = re.split("\s", pattern, 1)
            name = pattern[1]
            type1 = pattern[2]
            type2 = pattern[3]
            total = pattern[4]
            hp = pattern[5]
            attack = pattern[6]
            defense = pattern[7]
            sp_atk = pattern[8]
            sp_def = pattern[9]
            speed = pattern[10]
            gen = pattern[11]
            legendary = pattern[12]


          #osv.


      #skapar objekt
            pokemon_ob = Pokemon(name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary)


  #lagrar objekt i en lista
            poke_list.append(pokemon_ob)
            #print(poke_list)
    search(poke_list)

  #returnerar listan
    return poke_list
#search(poke_list)
print(poke_list)