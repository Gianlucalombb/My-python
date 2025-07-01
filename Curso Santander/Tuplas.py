"""
 Tuplas en Python
Una tupla es muy parecida a una lista, pero con una diferencia clave: las tuplas no se pueden cambiar una vez creadas. Esto significa que no podés agregar, eliminar ni modificar sus elementos.

Se escriben con paréntesis ( ).

Guardan varios elementos ordenados, separados por comas.

🔨 Crear y usar tuplas
punto = (3, 4)
Para acceder a un elemento usás el índice igual que en listas, empezando en 0:

print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4
 Inmutabilidad
No podés cambiar los elementos de una tupla, por ejemplo:
punto[0] = 5 da error.

Son útiles cuando querés guardar datos que no deben cambiar, como coordenadas, configuraciones, etc.

Métodos útiles de tuplas
Aunque no podés modificarla, podés usar estos métodos para trabajar con tuplas:

count(elemento): cuenta cuántas veces aparece un elemento.

index(elemento): te dice en qué posición aparece por primera vez un elemento (podés buscar desde dónde hasta dónde).

También podés usar la función len(tupla) para saber cuántos elementos tiene.

Ejemplo
mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.index(2))      # Imprime 1 (la primera vez que aparece el 2)
print(mi_tupla.index(2, 2))   # Imprime 3 (busca el 2 empezando en el índice 2)
print(mi_tupla.index(2, 2, 4))# Imprime 3 (busca el 2 entre los índices 2 y 4)
"""
"""
Ejercicio 1
Crea una tupla con los números del 1 al 5 e imprimí el tercer elemento.

numeros = (1, 2, 3, 4, 5)

print(numeros[2])
"""
"""
Ejercicio 2
Dada la tupla (10, 20, 30, 40, 50), mostrá cuántos elementos hay y en qué posición está el número 40.

tupla = (10, 20, 30, 40, 50)

print(len(tupla))

print(tupla.index(40))
"""

"""
 Ejercicio 3
Contá cuántas veces aparece el número 3 en esta tupla:
(1, 3, 5, 3, 7, 3, 9)
"""

mi_tupla = (1, 3, 5, 3, 7, 3, 9)

print(mi_tupla.count(3))