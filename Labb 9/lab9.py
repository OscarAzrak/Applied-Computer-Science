from linkedQFile import LinkedQ

atomlist = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
            'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class SyntaxError(Exception): #Eget exceptionfel
    pass

def skapaQ(formel):
    q = LinkedQ()
    for i in formel:
        q.enqueue(i)
    #lägger till . i slutet för att avsluta while-loop
    q.enqueue(".")
    return q

def checkMol(q):
    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except SyntaxError as felmeddelande:
        return str(felmeddelande)

def readFormel(q):
    while q.peek() != ".":
        readMol(q)

def readMol(q):
    readGroup(q)
    if readFirst(q.peek()) or q.peek() == "(":
        readMol(q)

def readGroup(q): #kollar om första i kön börjar med parantes annars körs readAtom funktionen
    if q.peek() == "(":
        q.dequeue()
        readMol(q)
        if q.peek() == ")":#om det inte finns en siffra efter slutparantesen ger felmeddelande
            q.dequeue()
            if q.peek().isnumeric():
                readNumber(q)
            else:
                raise SyntaxError("Saknad siffra vid radslutet " + printRest(q))
        else:
            raise SyntaxError("Saknad högerparentes vid radslutet " + printRest(q))
    elif readFirst(q.peek()) or readSecond(q.peek()):
        readAtom(q)
    else:
        raise SyntaxError("Felaktig gruppstart vid radslutet " + printRest(q))

def readAtom(q):
    #kollar om första symbolen är stor bokstav
    fir = q.dequeue()
    # om den är stor, går vidare i if-satsen
    if readFirst(fir):
        # kollar om det finns en andra bokstav, då lägs de ihop atombokstäverna till en atom och
        # kollar om atomen finns i atomlistan
        if readSecond(q.peek()):
            sec = q.dequeue()
            atom = fir + sec
            if atom not in atomlist:
                raise SyntaxError("Okänd atom vid radslutet " + printRest(q))
        else:
            #om bara en bokstav finns kollas denna i atomlistan
            if fir not in atomlist:
                raise SyntaxError("Okänd atom vid radslutet " + printRest(q))
        #om nästa är en siffra anropas funktionen Readnumber
        if q.peek().isnumeric():
            readNumber(q)
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet " + fir + printRest(q))

def readFirst(x): #returnar true eller false om den första är stor eller liten bokstav
    return x.isupper()

def readSecond(x): #returnar true eller false om den andra är stor eller liten
    return x.islower()

def readNumber(q): #kollar siffrorna som är kvar i kön
    num = q.dequeue()
    if int(num) == 0:
        raise SyntaxError("För litet tal vid radslutet " + printRest(q))
    elif num.isnumeric():
        while q.peek().isnumeric():
            nextNum = q.dequeue()
            num += nextNum
        if int(num) < 2:
            raise SyntaxError("För litet tal vid radslutet " + printRest(q))
    else:
        raise SyntaxError("Saknad siffra vid radslutet " + num + printRest(q))

def printRest(q):
    rest = ""
    while not q.isEmpty() and q.peek() != ".":
        symb = q.dequeue()
        rest += symb
    return rest

def main():
    formel = input().strip()
    while formel != "#":
        try:
            q = skapaQ(formel)
            result = checkMol(q)
            print(result)
            formel = input().strip()
        except SyntaxError:
            formel = input().strip()

if __name__ == "__main__":
    main()