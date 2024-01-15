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
        index = self.hashfunction(key)
        node = self.array[index]
        while True:
            if node is None:
                self.array[index] = HashNode(key, data)
                break
            elif node is not None:
                if node.key == key:
                    self.array[index] = HashNode(key,data)
                    break
                elif node.next == None:
                    node.next = HashNode(key, data)
                    break
                elif node.next != None:
                    node = node.next


                #slutnode = krockhantering(node)
                #slutnode.next = HashNode(key, data)
                

    def search(self, key):
        index = self.hashfunction(key)
        node = self.array[index]
        while True:
            if node is None:
                raise KeyError
            elif node.key == key:
                return node.data
            else:
                node = node.next

            """elif node.next is not None:
                while node.next is not None:
                    if node.key == key:
                        return node.data
                    else:
                        slutnode = krockhantering(node)"""
        
        
    def __getitem__(self, key):
        return self.search(key)
    

    def hashfunction(self, key):
        h = ""
        for a in key:
            val = ord(a)
            h = h + str(val)
        y = len(self.array)
        return int(h) % y


h = HashTable(1)
h.store("Jakob", "bord")
h.store("Hania", "stol")
print(h["Hania"])
h.store("Hania", "säng")
print(h["Hania"])

print(h["Jakob"])
print(h["Hania"])




