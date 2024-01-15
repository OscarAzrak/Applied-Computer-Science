from linkedQFile import LinkedQ
import string

class FormelError(Exception):
    pass

class Validator:

    def atom_valid(self, formel):
        q = LinkedQ()

        for i in formel:
            q.enqueue(i)

        #kollar om första symbolen är liten bokstav, om den är det ger FormelError
        if q.peek().isnumeric():
            raise FormelError

        if q.peek() not in string.ascii_uppercase:
            raise FormelError
        else:
            q.dequeue()
        if q.length() < 1:
            pass
        else:
            while q.peek().isalpha():
                if q.peek() in string.ascii_uppercase:
                    raise FormelError
                else:
                    q.dequeue()
        print(q.length())

        if q.peek().isnumeric:
            if q.length() > 2:
                if int(q.peek()) < 1:
                    raise FormelError
                else:
                    q.dequeue()
                    print(q.length())
            if q.length() > 2:
                if int(q.peek()) < 1:
                    print(q.length())
                    raise FormelError

        return True








""""
        #kollar om den
        if q.peek() not in string.ascii_uppercase:
            raise FormelError
        else:
            if q.length() > 1:
                q.dequeue()
        #kollar om andra bokstaven är stor, ger FormelError
        if q.peek() in string.ascii_uppercase:
            raise FormelError

        #kollar om andra bokstaven är liten, dequear så kollar vi siffror sen
        if q.peek().islower():
            q.dequeue()
        try:
            #om tex formeln har tre bokstäver dequar vi tills vi får siffrorna
            while not q.peek().isnumeric():
                q.dequeue()

            #om första siffran är mindre än 1
            if int(q.peek()) < 1:
                raise FormelError

            elif int(q.peek()) < 2:
                q.dequeue()
                if q.peek() is None:
                    raise FormelError
        except:
            pass


        return True"""

