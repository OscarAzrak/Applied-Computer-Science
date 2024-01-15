

class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data
        self.next = None

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
        node = self.array[index]

        if node is not None:
            if self.array[index].key == key:
                self.array[index] = HashNode(key,data)
                pass
            else:
                node.next = HashNode(key, data)
        elif node is None:
            # Skapa noden och lägg in nyckeln och värdet
            self.array[index] = HashNode(key, data)
            # print(self.array[index])
        else:

            node.next = HashNode(key, data)
            return node.next
        """while node is not None:
            if node.key == key:
                node = HashNode(key, data)
            old = node
            node = node.next"""

            #old.next = HashNode(key, data)
        """while True:
            if node is None:
                #Skapa noden och lägg in nycjkeln och värdet
                self.array[index] = HashNode(key, data)
                #print(self.array[index])
                break

            # om nodens key är samma så byts value ut
            elif self.array[index].key == key:
                self.array[index] = HashNode(key, data)
                break
            else:
                for x in self.array[index]:
                    #If key is found, then update
                    # its current value to the new value.
                    if x[0] == key:
                        x[1] = data
                        break

                #node.next = HashNode(key, data)




                #q = LinkedQ()
                #self.array[index] =
                #q.enqueue()
                #HashNode(key, data)
            #krock"""



    def search(self, key):
        #få hashvärde
        index = self.hashfunction(key)
        node = self.array[index]

        while node is not None and node.key != key:
            node = node.next
        if node is None:
            raise KeyError
        else:
            return node.data



    def __getitem__(self, key):
    # anropar search-metoden så att man kan skriva d[key] istället för d.search(key)
        return self.search(key)


    def hashfunction(self, key):
        h = ""
        for a in key:
            val = ord(a)
            h = h + str(val)
        """key: nyckeln
        Beräknar hashfunktionen för key"""
        #x = hash(key)
        y = len(self.array)
        return int(h) % y

def nodpekare(nod):
    while nod.next is not None:
        slutnod = nod.next
        nodpekare(slutnod)
        return slutnod

"""h = HashTable(1)
h.store("Jakob", "bord")
h.store("Hania", "stol")
h.store("Hania", "säng")

print(h["Jakob"])
print(h["Hania"])"""




