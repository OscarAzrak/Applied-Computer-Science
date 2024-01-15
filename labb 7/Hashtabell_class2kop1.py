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
        self.array = [None]*self.size

    def __str__(self):
        return str(self.array)

    def store(self, key, data):
        index = self.hashfunction(key)
        node = self.array[index]
        # om noden är None

        if node is None:
            #Skapa noden och lägg in nycjkeln och värdet
            self.array[index] = HashNode(key, data)
            #print(self.array[index])
            pass

        # om nodens key är samma så byts value ut
        elif self.array[index].key == key:
            self.array[index] = HashNode(key, data)

        else:
            while node.next != None:
                node.next = node.next.next
            node.next = HashNode(key, data)



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
        y = len(self.array)
        return int(h) % y


#h = HashTable(1)
#h.store("Jakob", "bord")
#h.store("Hania", "stol")
#h.store("Hania", "Säng")
#
#print(h["Jakob"])
#print(h["Hania"])




