from molgrafik import *

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
    def __str__(self):
        return str(self.atom), str(self.num)

#Bygger upp träd för "C(OH)2"
ruta1 = Ruta("Si")
print(ruta1)

ruta2 = Ruta(num=4)

ruta1.next = ruta2
ruta3 = Ruta(atom = "C", num = 3)

ruta2.down = ruta3
ruta4 = Ruta(num=2)

ruta3.next = ruta4
ruta5 = Ruta("C")
ruta4.down = ruta5
ruta6 = Ruta("O")
ruta5.next = ruta6
ruta7 = Ruta("O")
ruta6.next = ruta7
ruta8 = Ruta("H")
ruta7.next = ruta8

ruta9 = Ruta(num=7)
ruta2.next = ruta9
ruta10 = Ruta(atom = "H", num=2)
ruta9.down = ruta10
ruta11 = Ruta("O")
ruta10.next = ruta11



molekyl = ruta1

mol = Ruta(atom = "Cl", num = 2)
mg = Molgrafik()
mg.show(molekyl)

