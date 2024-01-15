class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data


    def __str__(self):
        return self.data

class HashTable:
    def __init__(self, size):
        self.size = size
        """size: hashtabellens storlek"""
        self.array = [None]*self.size

    def __str__(self):
        return str(self.array)

    def store(self, key, data):
        """key:nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""

        # Få hashvärde

        index = self.hashfunction(key)

        # om noden är None

        if self.array[index] is None:
            #Skapa noden och lägg in nyckeln och värdet
            self.array[index] = HashNode(key, data)
            #print(self.array[index])
            return

        # om nodens key är samma så byts value ut
        elif self.array[index].key == key:
            self.array[index] = HashNode(key, data)
        #krock

    def search(self, key):
        #få hashvärde
        index = self.hashfunction(key)

        if self.array[index] is not None:
            #finns ej
            return self.array[index].data
        elif self.array[index] == key:
            return self.array[index].data
        else:
            # hittat returnar value
            raise KeyError

    def __getitem__(self, key):
    # anropar search-metoden så att man kan skriva d[key] istället för d.search(key)
        return self.search(key)

    def hashfunction(self, key):
        """key: nyckeln
        Beräknar hashfunktionen för key"""
        x = hash(key)

        y = len(self.array)
        return x % y




