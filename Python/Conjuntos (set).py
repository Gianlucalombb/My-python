"""
¿Qué es un conjunto?
Un conjunto (set) es una estructura parecida a una lista, pero con 3 características importantes:

No tiene orden (no podés acceder con índices).

No se repiten los elementos (todo lo que pongas se guarda una sola vez).

Es mutable: podés agregar o sacar elementos.

🛠 Cómo crear un conjunto
Podés hacerlo de dos formas:
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
🧮 Operaciones entre conjuntos
Python te deja hacer operaciones como en matemáticas:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2 → Junta todo, sin repetir → {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2 → Lo que tienen en común → {3}

diferencia = conjunto1 - conjunto2 → Lo que tiene el primero pero no el segundo → {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2 → Todo menos lo que tienen en común → {1, 2, 4, 5}

Métodos útiles

frutas = {"manzana", "banana", "naranja"}
frutas.add("pera") → agrega un elemento

frutas.remove("banana") → elimina un elemento (falla si no existe)

frutas.discard("uva") → elimina si está, si no está no pasa nada

frutas.clear() → vacía todo el conjunto → queda como set()

🎯 Diferencia con otras estructuras:
Estructura	Ordenada	Mutable	Elementos repetidos	Acceso por índice
Lista	✅	✅	✅	✅
Tupla	✅	❌	✅	✅
Diccionario	❌ (solo claves)	✅	❌ (claves únicas)	❌ (se accede por clave)
Conjunto	❌	✅	❌ (únicos)	❌
"""

"""
Ejercicio 1: Eliminar duplicados de una lista
Dada la siguiente lista con elementos repetidos:

numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]

numeros = set(numeros)
print(numeros)
"""

"""
Ejercicio 2 — Comparación de conjuntos
Crea dos conjuntos:
amigos_juan = {"Ana", "Luis", "Carlos", "Marta"}
amigos_maria = {"Carlos", "Marta", "Pedro", "Sofía"}
Hacé lo siguiente:

Mostrá los amigos que tienen en común Juan y María.

Mostrá los amigos que solo tiene Juan.

Mostrá todos los amigos de ambos sin repetir.

amigos_juan = {"Ana", "Luis", "Carlos", "Marta"}
amigos_maria = {"Carlos", "Marta", "Pedro", "Sofía"}

# Amigos en común
interseccion = amigos_juan & amigos_maria
print("Amigos en común:", interseccion)

# Amigos que solo tiene Juan
solo_juan = amigos_juan - amigos_maria
print("Amigos que solo tiene Juan:", solo_juan)

# Todos los amigos sin repetir
union = amigos_juan | amigos_maria
print("Todos los amigos sin repetir:", union)
"""
"""
Ejercicio 3 — Verificar subconjunto
Instrucciones:
Dado un conjunto con permisos de un usuario y otro conjunto con los permisos requeridos para acceder a una página, escribí un programa que verifique si el usuario tiene todos los permisos necesarios. Si los tiene, imprimir "Acceso concedido"; si no, imprimir "Acceso denegado".

permisos_usuario = {"Leer", "Escribir", "Remplazar"}
permisos_requeridos = {"Leer", "Escribir"}

if permisos_requeridos.issubset(permisos_usuario):
    print("Acceso concedido")
else:
    print("Acceso denegado")

A.issubset(B) verifica si todos los elementos del conjunto A están dentro del conjunto B.

"""