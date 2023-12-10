def bubblesort(lista):
    #Para obtener la longitud hasta el penultimo
    n = len(lista) -1

    #Ciclo para las pasadas (el 0 es el indice)
    for i in range (0, n):
        #Ciclo para comparar e intercambiar
        for j in range (0, n):
            if lista [j] > lista [j +1]:
                aux = lista [j]
                lista [j] = lista [j + 1]
                lista [j + 1] = aux
    return lista

scores = [70, 8, 0, 124, 45]

bubblesort(scores)

print ('Numeros antes de ordenar:', scores)
print ('Numeros ordenados', bubblesort(scores))
