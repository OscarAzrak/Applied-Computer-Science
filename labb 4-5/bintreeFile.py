class Node():
    def __init__(self, val, left = None, right =  None):
        self.value = val
        self.left = left
        self.right = right

    def putta(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left:
                return self.left.putta(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.putta(value)
            else:
                self.right = Node(value)
                return True

    def skriv(self):
        if self:
            if self.left:
                self.left.write()
            print(str(self.value))
            if self.right:
                self.right.write()
            print(str(self.value))

    def finns(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left:
                return self.left.finns(value)
            else:
                return False
        else:
            if self.right:
                return self.right.finns(value)
            else:
                return False

class Bintree():
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        #sorterar in newvalue i trädet
        if self.root:
            return self.root.putta(newvalue)
        else:
            self.root = Node(newvalue)
            return True


    def __contains__(self, value):
        if self.root:
        #True om value finns in trädet, False annars
            return self.root.finns(value)
        else:
            return False

    def write(self):
        #Skriver ut trädet i inorder
        #print("InOrder")
        self.root.skriv()
        #skriv(self.root)
        print("\n")






