def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])


listan = [1,2,3,4,5]
utskrift(listan)