"""
¿Qué es un bucle?
Un bucle sirve para repetir un bloque de código varias veces.
Esto es útil cuando querés hacer lo mismo muchas veces sin escribirlo de nuevo.

Bucle for
Se usa para recorrer cosas como listas, cadenas o cualquier cosa que tenga varios elementos.

Ejemplo:
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
📌 ¿Qué pasa acá?

frutas es una lista con 3 elementos.

El bucle for agarra uno por uno esos elementos.

La variable fruta va tomando esos valores: primero "manzana", después "banana", después "naranja".

Con cada valor, se ejecuta el código de adentro del bucle. En este caso: print(fruta), que imprime el nombre de la fruta.

🧠 Así podés recorrer:

Listas: ["a", "b", "c"]

Cadenas: "Hola" → recorre letra por letra

Rangos de números: range(5) → 0, 1, 2, 3, 4

Ejemplo con range:

for i in range(5):
    print(i)
Esto imprime:
0  
1  
2  
3  
4
🔁 Bucle while (explicado fácil)
Se usa cuando querés repetir algo mientras se cumpla una condición.

Ejemplo:
contador = 0

while contador < 5:
    print(contador)
    contador += 1
📌 ¿Qué pasa acá?

Empezamos con contador = 0.

El while pregunta: ¿contador es menor que 5?

Si es sí, entra al bucle, imprime el número, y le suma 1.

Repite esto hasta que contador ya no sea menor que 5.

Cuando llega a 5, la condición ya no se cumple y el bucle se corta.

🎯 Resumen rápido:
while
Lo usás cuando no sabés cuántas veces se va a repetir algo.

Se repite mientras una condición sea verdadera.

Ejemplo: esperar que el usuario escriba “salir” para cortar.

for
Lo usás cuando sabés cuántas veces querés repetir.

Recorre una secuencia (como números, lista, cadena) un número fijo de veces.

Ejemplo: imprimir “Hola” 10 veces.


"""

"""
Control de bucles en Python
-break
Sirve para salir inmediatamente de un bucle, aunque la condición siga siendo verdadera.
Cuando Python encuentra un break, termina el bucle y sigue con el código que está afuera.

Ejemplo:
contador = 0

while True:  # bucle infinito (se repite siempre)

    print(contador)
    contador += 1

    if contador == 5:
        break  # sale del bucle cuando contador llega a 5
Esto imprime:
0
1
2
3
4
Y luego sale del bucle.

-continue
Sirve para saltar lo que queda en la vuelta actual del bucle y pasar a la siguiente repetición.

Ejemplo:
for i in range(10):

    if i % 2 == 0:
        continue  # salta a la siguiente vuelta si i es par

    print(i)
Esto imprime solo los números impares:
1
3
5
7
9
3-pass
Es un “no hacer nada”. Sirve cuando Python necesita que haya una instrucción, pero vos todavía no querés poner nada ahí. Es un marcador de posición.
for i in range(5):
    pass  # por ahora no hacemos nada en este bucle
✅ Resumen final
break: termina el bucle ahora mismo.

continue: salta lo que queda en esta vuelta y sigue con la siguiente.

pass: no hace nada, solo ocupa lugar para que el código esté correcto.
"""

"""
Ejercicio 1: Números del 1 al 10
Mostrá en pantalla los números del 1 al 10 usando un bucle for.

for contador in range(1, 11):
    print(contador) 
"""

"""
Ejercicio 2: Suma de los primeros N números
Pedí al usuario un número entero n y usá un bucle while para calcular la suma de los primeros n números naturales (1 + 2 + ... + n).

n = int(input("Ingrese un número: "))
contador = 1
suma = 0

while contador <= n:
    suma += contador
    contador += 1

print("La suma es:", suma)
"""

"""
frutas = ["manzana", "banana", "mandarina"]

for fruta in frutas:
    print(fruta)
"""
"""
dinero = 100

while dinero <= 500:
    print(dinero)
    dinero += 20
"""