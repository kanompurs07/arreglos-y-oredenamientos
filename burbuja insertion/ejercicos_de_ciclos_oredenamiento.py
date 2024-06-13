ejercicos 

# dado la siguiente lista de nombres desordenados:
# [juan,ana, carlos, elena, pedro]
# utiliza el algoritmo de burbuja para ordenalos alfabeticamente 


"""
nombres = ["juan","ana","carlos","elena","pedro"]

print("la lista de los nombres antes ordenar: ", nombres)
# algoritmo de la burbuja

n = len(nombres)
for i in range(n):
    intercambio = False
    for j in range (n -1 -i):
        if nombres[j] > nombres[j+1]:
            nombres[j], nombres[j+1] = nombres[j + 1], nombres [j]
            intercambio = True
        if not intercambio:
            break 
print(" la lista de nombre despues de ordenar es:", nombres)
"""


# ejercicos 2 
# dados los siguientes nombres [luis,maria, david, laura , andres]
# utilizar el algoritmo de insertion para ordenalos alfabeticamente 

"""
nombres = ["luis","maria","david","laura","andres"]

print(" lista de nombres antes de ordenar:",nombres)

n = len(nombres)
for i in range(1,n):
    valor_actual = nombres[i]
    j = i -1
    while j >= 0 and nombres[j] > valor_actual:
        nombres [j+1] = nombres[j]
        j-= 1
        nombres[j+1] = valor_actual
print(" la lista de nombres despues de ordenar es:",nombres )
"""