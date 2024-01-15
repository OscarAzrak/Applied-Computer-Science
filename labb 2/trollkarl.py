from array import array
from linkedQFile import LinkedQ
q = LinkedQ()


#frågar om vilken ordning korten ska vara, 7,1,12,2,8,3,11,4,9,5,13,6,10
ordn = input()
#tar bort komma tecken samt gör det till en lista
ordn = ordn.split(' ')


#lägger in de i kön i ordningen man skrivit
for elem in ordn:
    q.enqueue(elem)
#lägger första kortet sist och lägger ner nästa kort
lista = []
for bb in range(0, len(ordn)):
    y = q.dequeue()
    q.enqueue(y)
    u = q.dequeue()
    lista.append(u)
print(" ".join(lista))
