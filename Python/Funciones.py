"""
¿Qué es una función?
Una función es como una mini-máquina dentro de tu código.
Le das algo → hace una tarea → y te da un resultado (o simplemente hace algo).

Sirve para no repetir código y para organizar mejor tu programa.

¿Cómo se crea una función?
Usás la palabra def, le ponés un nombre, paréntesis, y dos puntos:
def saludo():
    print("¡Hola, mundo!")

Y para usarla (llamarla), simplemente escribís su nombre con paréntesis:
saludo()  # Imprime ¡Hola, mundo!
Parámetros (lo que le das)

Podés hacer que una función reciba datos:
def saludo(nombre):
    print(f"¡Hola, {nombre}!")
La usás así:

saludo("Juan")   # ¡Hola, Juan!
saludo("María")  # ¡Hola, María!
📤 return (lo que te devuelve)
Si querés que una función te devuelva un valor para usarlo después:

def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7
⚡ Funciones rápidas (lambda)
Una lambda es una función chiquita de una sola línea:

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25
Se usa cuando necesitás algo rápido y simple.

🌍 Alcance de variables
Global: creada fuera de funciones → se puede usar en todo el código.

Local: creada dentro de una función → solo existe dentro de esa función.

variable_global = 20

def funcion():
    variable_local = 10
    print(variable_local)  # OK

def funcion2():
    print(variable_global)  # OK

print(variable_global)  # OK
print(variable_local)  # ❌ Error, no existe fuera de la función
📝 Documentar funciones (docstrings)
Esto se hace para explicar qué hace una función, qué recibe y qué devuelve.

def area_rectangulo(base, altura):
    Calcula el área de un rectángulo.

    Args:
        base (float): La base.
        altura (float): La altura.

    Returns:
        float: El área.
    return base * altura
🔢 Funciones con muchos argumentos
Podés hacer una función que reciba cualquier cantidad de números con *:
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))        # 6
print(suma_variable(4, 5, 6, 7))     # 22
✅ En resumen
def nombre(): → definís una función.

return → devuelve un valor.

*args → sirve para pasar muchos datos.

lambda → una función rápida y de una sola línea.

Variables locales viven dentro de la función.

Las funciones ayudan a organizar, reutilizar y simplificar tu código.
"""

"""
Ejercicio 1 — Función saludo simple
Define una función llamada saludo que reciba un parámetro nombre y que imprima en pantalla:
¡Hola, {nombre}!

Luego llama a la función pasando diferentes nombres.

def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("gian")
saludo("gustavo")
"""
"""
Ejercicio 2 — Función suma
Define una función llamada suma que reciba dos números como parámetros y devuelva la suma de ambos.

Luego, llama a la función con dos números y muestra el resultado.

def suma(numero):
    print(numero + numero)

suma(1)
suma(5)
"""

"""
Ejercicio 3 — Función que calcula el área de un rectángulo
Define una función llamada area_rectangulo que reciba la base y la altura y devuelva el área del rectángulo (base * altura).
Llama a la función con valores de base y altura y muestra el resultado.

def area_rectangulo(base, altura):
    return base * altura

# Ejemplo de uso:
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

resultado = area_rectangulo(base, altura)
print(f"El área del rectángulo es: {resultado}")
"""
