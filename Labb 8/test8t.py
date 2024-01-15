from array import array
from linkedQFile import LinkedQ
import string
import sys
q = LinkedQ()
ATOMER = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]

class FormelError(Exception):
    pass

formel = input()

#lägger in de i kön i ordningen man skrivit
for elem in formel:
    q.enqueue(elem)


def readNum():
    """Reads digits larger than 1. Raises exception if condition is not fulfilled."""
    try:
        if int(q.peek()) >= 2:
            print(q.peek())
            q.dequeue()
            return
        else:
            q.dequeue()
            print("Too small digit at the end of row: "+getRest())
            sys.exit()
    except (ValueError,TypeError):
        raise FormelError("Not a number.")

def readletter():
    """Reads lowercase letters and returns them."""
    if q.peek() in string.ascii_lowercase:
        print(q.peek())
        return q.dequeue()
    else:
        raise FormelError("Expected lowercase letter.")

def readLetter():
    """Reads capital letters and returns them."""
    if q.peek() in string.ascii_uppercase:
        print(q.peek())
        return q.dequeue()
    else:
        raise FormelError("Expected capital letter.")

def readAtom():
    """Reads atoms on the form X and Xx. Raises Exception if the format for an atom is not fulfilled or if the atom does not exist."""
    X = ""
    try:
        X += readLetter()
    except FormelError:
        print("Missing capital letter at end of row: "+getRest())
        sys.exit()
        return

    try:
        x = readletter()
        atom = X+x
    except (FormelError, TypeError):
        atom = X

    if atom in ATOMER:
        return
    else:
        raise FormelError("Unknown atom.")


def getRest():
    rest = ""
    while not q.isEmpty():
        rest += q.dequeue()
    return rest
readAtom()