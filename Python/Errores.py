"""
Errores comunes en Python
Estos errores te pueden aparecer cuando algo está mal en tu código. Pero no te asustes: todos los programadores los cometen. Lo importante es saber reconocerlos.

❌ 1. SyntaxError (Error de sintaxis)
Te olvidaste de escribir bien algo que Python necesita para entenderte.

def mi_funcion()  # ❌ falta el ":" al final
    print("Hola")
✅ Solución:
def mi_funcion():
    print("Hola")

❌ 2. NameError (Error de nombre)
Estás usando una variable o función que no existe o no está definida todavía.
print(variable_no_definida)  # ❌
✅ Solución:
variable_no_definida = "Hola"
print(variable_no_definida)  # ✅

❌ 3. TypeError (Error de tipo)
Estás mezclando cosas que no se pueden mezclar, como sumar un número con un texto.
resultado = 5 + "10"  # ❌ número + texto = error
✅ Solución:
resultado = 5 + int("10")  # ✅ convierto el texto a número
print(resultado)  # Imprime 15

❌ 4. IndexError (Error de índice)
Querés acceder a una posición de una lista que no existe.

lista = [1, 2, 3]
print(lista[3])  # ❌ la lista va de 0 a 2
✅ Solución:
print(lista[2])  # ✅ este sí existe
"""