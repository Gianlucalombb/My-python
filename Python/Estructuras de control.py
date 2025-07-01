"""
-Estructuras condicionales
Las estructuras condicionales permiten que tu programa tome decisiones. Es decir, que haga algo solo si se cumple una condición.

if
Se usa para ejecutar algo si la condición es verdadera.

edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
En este ejemplo, si la edad es 18 o más, se imprime el mensaje.
Si no lo es, no pasa nada (el bloque se salta).

if-else
Se usa cuando querés que pase una cosa si la condición es verdadera, y otra cosa si es falsa.

edad = 15

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
Acá, si la edad es menor que 18, entra al else y muestra otro mensaje.

if-elif-else
Se usa cuando tenés más de una condición para verificar, como un menú de opciones.

calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")
El programa va evaluando las condiciones en orden.
Cuando encuentra una verdadera, ejecuta ese bloque y ya no sigue con las demás.

Tip:

Podés usar solo if.

Podés usar if con else.

O podés usar if con varios elif y un else final, que se ejecuta solo si nada anterior se cumplió.
"""
"""
Ejercicio 1 — Estructuras de control
Instrucciones:
Escribí un programa que pida al usuario un número entero y diga si es:
numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
"""
"""
Ejercicio 2 — Estructuras de control con múltiples condiciones
Instrucciones:
Escribí un programa que pida al usuario ingresar su edad y luego muestre:
"""

"""
Edad = int(input("Ingrese su edad: "))

if Edad < 12:
    print("Eres un niño")
elif 12 <= Edad <= 17:
    print("Eres un adolescente")
elif 18 <= Edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
"""

"""
Ejercicio 3 — Calificación con letras
Instrucciones:
Escribí un programa que pida al usuario un puntaje (de 0 a 100) y muestre la calificación según esta escala:


puntaje = int(input("Ingrese un puntaje del 0 al 100: "))

if 90 <= puntaje <= 100:
    print("Excelente")
elif 80 <= puntaje <= 89:
    print("Muy bueno")
elif 70 <= puntaje <= 79:
    print("Bueno")
elif 60 <= puntaje <= 69:
    print("Suficiente")
elif puntaje < 60:
    print("Insuficiente")
else:
    print("Puntaje Invalido")
"""
