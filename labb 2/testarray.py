from array import array


class ArrayQ:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
print(x)
y = q.dequeue()


if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")