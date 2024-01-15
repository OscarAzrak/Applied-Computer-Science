class Node:
    #value och next är = None eftersom första noden man insertar i listar kommer inte ha något att peka på
    def __init__(self,value):
        self.value = value
        self.next = None #Nästa värde har ingenting att peka på från början
    def __str__(self):
        return int(self.value)
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_data(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def enqueue(self, kort):
        node = Node(kort)
        if self.__size == 0:
            self.__first = node
        else:
            self.__last.set_next(node)
        self.__last = node
        self.__size += 1
        return
    def isEmpty(self):
        return self.__first == None



    #def listLength(self):
    #    count = 0
    #    curr_node = self.__first
    #
    #    while curr_node is not None:
    #        count += 1
    #        curr_node = curr_node.next
    #    return count
    #def printList(self):
    #    curr_node = self.__first
    #
    #    while curr_node is not None:
    #        print(curr_node.value)
    #        curr_node = curr_node.next
    #    return
    def dequeue(self):
        curr_node = self.__first
        prev_node = None
        curr_id = 1
        new_node = curr_node.next
        while curr_node is not None:
            if curr_id == self.__size:
                if prev_node is not None:
                    prev_node.next = curr_node.next
                else:
                    self.__first = curr_node.next
                    return
            prev_node = curr_node
            curr_node = curr_node.next
            self.__size -= 1




    #def dequeue(self):
    #    if self.__first is None:
    #        print("finns inget att radera")
    #        return
    #    self.__first = self.__first.next
    #
    #def size(self):
    #    return len(self.items)