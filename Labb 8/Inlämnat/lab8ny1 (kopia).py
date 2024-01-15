from linkedQFile import LinkedQ

class SyntaxError(Exception): #Eget exceptionfel
    pass

def skapaQ(formel):
    q = LinkedQ()
    for i in formel:
        q.enqueue(i)
    #lägger till . i slutet för att avsluta while-loop
    q.enqueue(".")
    return q

def checkAtom(q):
    try:
        readAtom(q)
        return "Formeln är syntaktiskt korrekt"

    except SyntaxError as felmeddelande:
        return str(felmeddelande)


def readAtom(q):
    while q.peek() != ".":
        #kollar om första symbolen är stor bokstav
        if readFirst(q.peek()):
            #om den är stor, dequear så vi kollar nästa
            q.dequeue()
            #om nästa symbol är liten bokstav dequear, så kolla om det finns siffra
            if readSecond(q.peek()):
                q.dequeue()
            #om nästa är en siffra anropas funktionen Readnumber
            if q.peek().isnumeric():
                readNumber(q)
        else:
            raise SyntaxError("Saknad stor bokstav vid radslutet " + printRest(q))


def readFirst(x): #returnar true or false om den första är stor eller liten bokstav
    return x.isupper()


def readSecond(x): #returnar true or false om den andra är stor eller liten
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
            result = checkAtom(q)
            print(result)
            formel = input().strip()
        except SyntaxError:
            formel = input().strip()

if __name__ == "__main__":
    main()