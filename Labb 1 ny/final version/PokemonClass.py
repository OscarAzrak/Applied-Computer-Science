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
        rep = "\nPokemon\n"
        rep += "name: " + str(self.name) + "\n" + "type1: " + str(self.type1) + "\n" + "type2: " + str(self.type2) + "\n" \
               + "total: " + str(self.total) + "\n" + "hp: " + str(self.hp) + "\n" + "attack: " + str(self.attack) + "\n" \
               + "defense" + str(self.defense) + "\n" + "sp_atk: " + str(self.sp_atk) + "\n" + "sp_def: " + str(self.sp_def) \
               + "\n" + "speed: " + str(self.speed) + "\n" + "gen: " + str(self.gen) + "\n" + "legendary: " + str(self.legendary) + "\n"
        return rep


    def __lt__(self, other):
        if self.attack < other.attack:
            return self.name + " has lower attack than " + other.name
        else:
            return self.name + " has greater attack than " + other.name


    def __gt__(self, other):
        if self.defense > other.defense:
            return self.name + " has greater defense than " + other.name
        else:
            return self.name + " has lower defense than " + other.name


    def __eq__(self, other):
        if self.gen == other.gen:
            return self.name + " and " + other.name + " belongs to the same generation."
        else:
            return self.name + " and " + other.name + " do not belong to the same generation."


