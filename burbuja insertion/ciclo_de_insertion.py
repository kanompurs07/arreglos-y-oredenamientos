# insertion sort
"""
def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        valor_actual = lista[i]
        j = i -1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista [j + 1] = valor_actual
        print(f"paso {i}: {lista}")

numeros = [7,2,4,1,9]
print("la lista de numero antes de ordenar:", numeros)

insertion_sort(numeros)

print("lista numero desoues de ordenar:" , numeros)
"""