"""
¿Qué es un módulo?
Un módulo es simplemente otro archivo de Python que tiene funciones, variables o clases que podés usar en tu código.

Por ejemplo:
Python ya trae muchos módulos listos para usar como:

math: funciones matemáticas

random: números aleatorios

datetime: fechas y horas

¿Cómo se usa un módulo?
Opción 1: importar todo el módulo
import math

print(math.sqrt(25))  # raíz cuadrada → 5.0
Usás el nombre del módulo (math) y luego la función (sqrt()).

Opción 2: importar solo lo que necesitás

from math import sqrt

print(sqrt(25))  # también imprime 5.0
Así no necesitás poner el nombre del módulo antes.

Ejemplo con módulo random
import random

print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
📅 Ejemplo con módulo datetime

import datetime

print(datetime.datetime.now())  # Muestra la fecha y hora actual
🧠 ¿Para qué sirven los módulos?
Para no tener que escribir todo desde cero

Para ordenar tu propio código (vos podés crear tus propios módulos)

Para usar funciones ya listas (como sqrt, randint, now, etc.)

📌 Resumen rápido
Acción	Código ejemplo
Importar todo un módulo	import math
Usar una función del módulo	math.sqrt(16)
Importar solo una función	from math import sqrt
Usar sin el nombre del módulo	sqrt(16)
"""

"""
¿Qué es un módulo personalizado?
Es simplemente un archivo .py donde escribís funciones, clases o variables para usar después en otros programas. Así podés organizar mejor tu código y reutilizarlo.

🛠️ Cómo crear y usar tu propio módulo
Creás un archivo nuevo con el nombre que quieras, por ejemplo mi_modulo.py.

Escribís funciones o lo que necesites dentro, por ejemplo:

# mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def calcular_suma(a, b):
    return a + b
En otro archivo Python (en la misma carpeta), importás ese módulo y usás sus funciones:

import mi_modulo

mi_modulo.saludar("Juan")  # Imprime: Hola, Juan!
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime: 8
🧩 Organización con varios módulos
Cuando el programa crece, es mejor dividir el código en varios módulos según su función.

Por ejemplo:

operaciones.py para funciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
utilidades.py para funciones generales
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")
💻 Usar esos módulos en tu programa principal
python
Copiar
Editar
import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")
📌 Beneficios
Código más ordenado y fácil de mantener

Funciones agrupadas según su función

Podés reutilizar módulos en otros proyectos
"""

"""
 ¿Qué es un paquete?
Un paquete es una carpeta (directorio) que agrupa varios módulos relacionados en una estructura ordenada. Así podés organizar mejor muchos módulos y evitar confusiones con nombres repetidos.

🛠️ Cómo crear un paquete
Crear una carpeta con el nombre que quieras, por ejemplo: mi_paquete

Dentro de esa carpeta, crear un archivo especial llamado __init__.py

Este archivo puede estar vacío (solo para que Python reconozca que esa carpeta es un paquete)

O puede contener código para inicializar el paquete.

Agregar tus módulos (.py) dentro de esa carpeta

Ejemplo de estructura:

markdown
Copiar
Editar
mi_paquete/
   __init__.py
   modulo1.py
   modulo2.py
📥 Cómo importar y usar módulos dentro de un paquete
En tu programa principal, podés importar así:

from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()
Si modulo1.py tiene una función funcion1() y modulo2.py tiene funcion2(), las podés usar llamándolas con el nombre del módulo.

📌 Resumen
Un paquete es una carpeta con módulos de Python adentro.

El archivo __init__.py hace que Python reconozca esa carpeta como un paquete.

Los paquetes te ayudan a organizar mejor tu código cuando tenés muchos módulos.

Importás módulos desde paquetes usando from paquete import modulo.
"""
