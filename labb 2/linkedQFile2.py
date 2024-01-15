class Node():
    #value och next är = None eftersom första noden man insertar i listar kommer inte ha något att peka på
    def __init__(self, value = None):
        self.value = value
        self.next = None    #Nästa värde har ingenting att peka på från början

    def __str__(self):
        return str(self.value)


class LinkedQ():
    def __init__(self, first = None, last = None):
        self.__first = first
        self.__last = last

    #returnerar True om första noden är None
    def isEmpty(self):
        return self.__first == None

    def enqueue(self, new_value):
        new_node = Node(new_value)
        if self.__first == None:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = new_node


    def dequeue(self):
        h = self.__first.value
        self.__first = self.__first.next
        return h








