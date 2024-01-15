class DictHash:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.d = {}


    def store(self, key, value):
        # lagrar data som value i dictionary, med nyckel som key
        self.d[key] = value

    def search(self, key):
        # slår upp nyckel i dictionary
        return self.d[key]

    def __getitem__(self, key):
    # anropar search-metoden så att man kan skriva d[key] istället för d.search(key)
        return self.search(key)


    def __contains__(self, key):
       # returnerar True om key finns i d, annars False
        if self.key:
            return True
        else:
            return False

