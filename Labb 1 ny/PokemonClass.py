class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = int(total)
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.sp_atk = int(sp_atk)
        self.sp_def = int(sp_def)
        self.speed = int(speed)
        self.gen = int(gen)
        self.legendary = legendary

    def __str__(self):
        rep = "Pokemon\n"
        rep += "name: " + str(self.name) + "\n" + "type1: " + str(self.type1) + "\n" + "type2: " + str(self.type2) + \
               "\n" + "total: " + str(self.total) + "\n" + "hp: " + str(self.hp) + "\n" + "attack: " + str(self.attack)\
               + "\n" + "defense" + str(self.defense) + "\n" + "sp_atk: " + str(self.sp_atk) + "\n" + "sp_def: " + \
               str(self.sp_def) + "\n" + "speed: " + str(self.speed) + "\n" + "gen: " + str(self.gen) + "\n" + \
               "legendary: " + str(self.legendary) + "\n"
        return rep

    def __lt__(self, other):
        return self.hp < other.hp
    
    def __gt__(self, other):
        return self.hp > other.hp
    
    def __eq__(self, other):
        return self.hp == other.hp
    def Printer(self, other):
        return self.name + "har mer hp än" + other.name

