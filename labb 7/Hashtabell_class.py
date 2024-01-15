class Node:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data

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
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for x in self.array[idx]:
                # If key is found, then update
                # its current value to the new value.
                if x[0] == key:
                    x[1] = data
                    break
            else:
                # If no breaks was hit in the for loop, it
                # means that no existing key was found,
                # so we can simply just add it to the end.
                self.array[idx].append([key, data])
        else:
            # This index is empty. We should initiate
            # a list and append our key-value-pair to it.
            self.array[idx] = []
            self.array[idx].append([key, data])

    def search(self, key):
        """key: nyckel
        Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError"""

        # 1. Compute hash
        index = self.hashfunction(key)
        # 2. Go to first node in list at bucket

        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does
            # then return its value.
            for x in self.array[index]:
                if x[0] == key:
                    return x[1]
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
        #
    def __getitem__(self, key):
    # anropar search-metoden så att man kan skriva d[key] istället för d.search(key)
        return self.search(key)

    def hashfunction(self, key):
        """key: nyckeln
        Beräknar hashfunktionen för key"""
        x = hash(key)
        y = len(self.array)
        return x % y



