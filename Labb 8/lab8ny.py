from linkedQFile import LinkedQ
import unittest
import string

class SyntaxError(Exception): #Eget exceptionfel vi lägger till för syntaxen
    pass
class Validator:

    def atom_valid(self, formel):
        q = LinkedQ()
        #lägger in varje symbol i formeln i kön

        for i in formel:
            q.enqueue(i)

        #kollar om första elementet ej är stor bokstav, ger fel om den ej är det.
        if q.peek() not in string.ascii_uppercase:
            print("Saknad stor bokstav vid radslutet", formel)
            return False
        else:
            #dequear så vi kollar på nästa symbol
            q.dequeue()
            #om inputet endast är N ger det oss att peek är None, sålänge den ej är None kör den if-satsen
            if q.peek() is not None:
                #om den andra suymbolen är en liten bokstav, dequear så vi kollar på nästa
                if q.peek() in string.ascii_lowercase:
                    q.dequeue()
                    #återigen kollar att formeln ej är t.ex H2, kollar om det är en siffta
                    if q.peek() is not None:
                        while q.peek().isalpha():
                            if q.peek() in string.ascii_uppercase:
                                raise SyntaxError
                            else:
                                q.dequeue()
                        if q.peek().isnumeric():
                            #om det endast finns en siffra i formeln
                            if q.length() < 2:
                                #om den siffran är mindre än 2, alltså 0,1 ger det oss fel t.ex Pb1
                                if int(q.peek()) < 2:
                                    print("För litet tal vid radslutet")

                                    raise SyntaxError
                            #annars finns det fler än en siffra, om den första siffran är mindre än 1, dvs 0 ger det oss fel
                            else:
                                if int(q.peek()) < 1:
                                    print("För litet tal vid radslutet")

                                    raise SyntaxError

        return print("Formeln är syntaktiskt korrekt")

def main():
    validator = Validator()

    formel = input().strip()
    while formel != "#":
        try:
            value = validator.atom_valid(formel)
            formel = input().strip()
        except SyntaxError:
            formel = input().strip()
            pass



if __name__ == "__main__":
    main()

