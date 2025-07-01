"""
¿Qué es una excepción?
Una excepción es un error que ocurre mientras tu código se está ejecutando.
En vez de que el programa se rompa, podés atrapar el error y hacer algo al respecto.

try - except
try:
Le dice a Python: "Intentá hacer esto... puede fallar".

except:
Y si falla, Python se salta al except y hace lo que vos le digas.

Ejemplo:

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
Acá, como 10 ÷ 0 da error, no se rompe el programa, sino que se imprime un mensaje de error.

🎯 ¿Y si puede fallar por varios motivos?
Podés tener varios except:

try:
    numero = int("hola")
except ZeroDivisionError:
    print("Error: división por cero")
except ValueError:
    print("Error: no se pudo convertir texto a número")

finally (opcional)
Este bloque siempre se ejecuta, pase lo que pase.
Se usa por ejemplo para cerrar archivos o liberar recursos:

try:
    archivo = open("archivo.txt", "r")
    # Leer el archivo...
except FileNotFoundError:
    print("Error: El archivo no existe")
finally:
    archivo.close()  # Esto se ejecuta sí o sí

✅ En resumen:
try: Intenta ejecutar algo que puede fallar.
except:	Maneja el error si ocurre. Podés tener uno o varios.
finally: Se ejecuta siempre (haya o no error), ideal para cerrar archivos o limpiar.
"""

"""
¿Qué es una excepción personalizada?
Es una excepción creada por vos mismo, para controlar errores especiales que solo tienen sentido dentro de tu programa.
Por ejemplo, si hacés un programa de banco y querés tirar un error cuando el saldo es insuficiente, podés crear una excepción llamada SaldoInsuficienteError.

🛠 ¿Cómo se hace?
Hay dos formas:

1. Con una excepción común (Exception)
def funcion():
    condicion = True
    if condicion:
        raise Exception("Pasó algo raro")

try:
    funcion()
except Exception as e:
    print(f"Error: {e}")
🔎 raise → sirve para lanzar un error
🔎 Exception("mensaje") → el mensaje que querés mostrar
🔎 as e → guarda el error en la variable e para mostrarlo después

🔸 2. Con una clase propia (la mejor forma)
class MiError(Exception):
    pass

def funcion():
    raise MiError("Este es mi error personalizado")

try:
    funcion()
except MiError as e:
    print(f"Ocurrió un error: {e}")
Acá estás creando una nueva clase de error (una nueva "excepción") que podés usar solo cuando la necesites.

✅ ¿Para qué sirve?
Te ayuda a:

Dar mensajes de error claros.

Detectar errores específicos de tu programa.

Que tu programa sea más ordenado, controlado y profesional.

🔒 Recordá:
raise = lanzar un error.

try = intento ejecutar algo.

except = si falla, manejo el error.

finally = se ejecuta siempre (ideal para cerrar archivos, etc.).

Podés hacer tu propio tipo de error con class TuError(Exception):.
"""
"""
Ejercicio 1 — División segura
Pedí dos números al usuario (dividendo y divisor) e imprimí el resultado de la división.
Si el usuario intenta dividir por 0, mostrá el mensaje: "Error: No se puede dividir por cero."
try:
    a = int(input("Ingresá el dividendo: "))
    b = int(input("Ingresá el divisor: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
"""

"""
Ejercicio 2 — Validar edad
Pedí al usuario su edad. Si escribe algo que no sea un número (por ejemplo, "hola"), mostrá un mensaje: "Error: Ingresá un número válido."
try:
    edad = int(input("Ingresá tu edad: "))
    print(f"Tenés {edad} años.")
except ValueError:
    print("Error: Ingresá un número válido.")
"""

"""
Ejercicio 3 — Usar finally
Abrí un archivo de texto llamado "notas.txt" en modo lectura.
Si el archivo no existe, mostrá un mensaje de error.
Usá finally para mostrar "Programa finalizado" siempre, pase lo que pase.
try:
    archivo = open("notas.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
finally:
    print("Programa finalizado.")
"""