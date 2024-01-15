
class HashTable:
    def __init__(self, size):
        self.size = size
        """size: hashtabellens storlek"""
        self.array = [None]*self.size

    def store(self, key, data):
        """key:nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""
        #hämta hash värde
        index = self.hashfunction(key)
        if self.array[index] is not None:
            #om indexet redan har ett värde där
            #om key redan finns kollar den om den är samma key
            #först kollar vi om det finns key
            for x in self.array[index]:
                # om key finns och är samma uppdateras
                if x[0] == key:
                    x[1] = data
                    break
            else:
                #om ingen break träffas i for loop, finns ingen key så då läggs key och värde i slutet

                self.array[index].append([key, data])
        else:
            #om index är tomt skapar vi en tom lista på den platsen och appendar vår key och värde i den
            self.array[index] = []
            self.array[index].append([key, data])

    def search(self, key):
        """key: nyckel
        Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError"""

        # 1. ta fram hash
        index = self.hashfunction(key)
        # 2. få till första noden i array

        if self.array[index] is None:
            raise KeyError
        else:
            #loopar igenom alla key value par
            #letar om vår key finns, om den gör det returnas värdet

            for x in self.array[index]:
                if x[0] == key:
                    return x[1]
            #om ingen return gjordes under loopen finns ingen key och keyerror raisas
            raise KeyError

    def __getitem__(self, key):
    # anropar search-metoden så att man kan skriva d[key] istället för d.search(key)
        return self.search(key)

    def hashfunction(self, key):
        h = ""
        for a in key:
            val = ord(a)
            h = h + str(val)
        y = len(self.array)
        return int(h) % y

