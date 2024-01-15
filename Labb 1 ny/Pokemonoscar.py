import csv
import codecs

pokemoner = []

class Pokemon:
    def __init__(self,name, typ_1, typ_2,Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary):
        self.name = name
        self.typ_1 = typ_1
        self.typ_2 = typ_2
        self.Total = int(Total)
        self.HP = int(HP)
        self.Attack = int(Attack)
        self.Defense = int(Defense)
        self.Sp_Atk = int(Sp_Atk)
        self.Sp_Def = int(Sp_Def)
        self.Speed = int(Speed)
        self.Generation = int(Generation)
        self.Legendary = Legendary

#f = open('pokemoninfo.csv.webarchive', 'r')
#with f:
#    row = csv.reader(f)
#    pokemoner.append(Pokemon(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))

def readFile(pokemoner):
    with open("pokemoninfo.csv.webarchive", "r") as f:
        line = f.readline().strip().split(",")
        while line != ['']:
            line = line[0].split(" ") + line[1:]
            pokemoner.append(Pokemon(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]))
            line = f.readline().strip().split(",")
readFile(pokemoner)
