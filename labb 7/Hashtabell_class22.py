class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, capacity):
        self.size = 0
        """size: hashtabellens storlek"""
        self.array = [None]*capacity

    def store(self, key, data):
        """key:nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""


        # 1. Increment size

        self.size += 1
        # 2. Compute index of key

        index = self.hashfunction(key)
        # Go to the node corresponding to the hash

        node = self.array[index]
        # 3. If bucket is empty:

        if node is None:
            # Create node, add it, return

            self.array[index] = HashNode(key, data)
            return
        else:
            if self.array[index].key == key:
                self.array[index] = HashNode(key, data)
        # 4. Collision! Iterate to the end of the linked list at provided index

        while node is not None:

            node = self.array[index+1]
        # Add a new node at the end of the list with provided key/value

        self.array[index+1] = HashNode(key, data)

    def search(self, key):
        # 1. Compute hash
        index = self.hashfunction(key)
        # 2. Go to first node in list at <rr<y>

        node = self.array[index]
        # 3. Traverse the linked list at this node

        while node is not None and node.key != key:

            node = self.array[index+1]

        # 4. Now, node is the requested key/value pair or None

        if node is None:
            # Not found
            raise KeyError
        else:
            # Found - return the data value

            return node.data
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



