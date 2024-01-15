

class HashTable:
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.array = [None]*size

    def store(self, key, data):
        """key:nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""
        idx = self.hashfunction(key)
        if self.array[idx] is not None:

            for x in self.array[idx]:

                if x[0] == key:
                    x[1] = data
                    break
            else:

                self.array[idx].append([key, data])
        else:

            self.array[idx] = []
            self.array[idx].append([key, data])





    def search(self, key):
        """key: nyckel
        Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError"""


        index = self.hashfunction(key)


        if self.array[index] is None:
            raise KeyError
        else:

            for x in self.array[index]:
                if x[0] == key:
                    return x[1]

            raise KeyError
        #
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
