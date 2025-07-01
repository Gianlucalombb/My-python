"""
Listas en Python
Una lista es como una caja donde guardás varios elementos juntos, ordenados uno después del otro.

Se escriben con corchetes [ ] y los elementos van separados por comas.

Los elementos pueden ser números, palabras, o cualquier cosa.

Ejemplo:
frutas = ["manzana", "banana", "naranja"]
🔢 Cómo acceder a los elementos de una lista
Cada elemento tiene una posición llamada índice que empieza en 0.

Para acceder a un elemento, usás el nombre de la lista y entre corchetes ponés el índice.
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"
También podés contar desde atrás con índices negativos:

print(frutas[-1])  # Imprime "naranja" (último elemento)
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"
🛠️ Métodos comunes para modificar listas
append(elemento): agrega un elemento al final.

insert(indice, elemento): agrega un elemento en la posición que quieras.

remove(elemento): elimina la primera vez que aparece ese elemento.

pop(indice): elimina y devuelve el elemento en la posición dada.

sort(): ordena la lista (por ejemplo, alfabéticamente o numéricamente).

reverse(): da vuelta la lista (el último pasa a ser primero).

Ejemplo paso a paso:

frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)          # ["manzana", "uva", "pera"]
print(fruta_eliminada) # "naranja"

frutas.sort()
print(frutas)  # ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # ["uva", "pera", "manzana"]
⚡ Listas de comprensión
Es una forma corta y rápida de crear una nueva lista transformando o filtrando elementos de otra lista.

La estructura es:
nueva_lista = [expresion for elemento in secuencia if condicion]
Ejemplo: Crear una lista con los cuadrados de los números pares:
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # [4, 16]
Aquí:

x ** 2 es el cuadrado de cada número.

if x % 2 == 0 significa “solo si el número es par”.
"""
"""
Ejercicio 1:
Crea una lista llamada numeros con estos números: [3, 7, 1, 9, 5]

Agrega el número 10 al final de la lista.

Elimina el número 7 de la lista.

Ordena la lista de menor a mayor.

Imprime la lista final.

numeros = [3, 7, 1, 9, 5]

numeros.append(10)
numeros.remove(7)
numeros.sort()

print(numeros)
"""
"""
Ejercicio 2 - Nombres favoritos

Crea una lista llamada nombres con 4 nombres que te gusten.

Agrega un nuevo nombre al final de la lista.

Cambia el segundo nombre de la lista por otro que te guste más.

Elimina el último nombre de la lista.

Imprime la lista final.
"""
