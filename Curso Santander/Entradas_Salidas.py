"""
Entrada (input)
Con input() le pedís datos al usuario.
Lo que escriba el usuario queda guardado en una variable.

nombre = input("¿Cómo te llamás? ")
print("Hola " + nombre)
El texto que aparece entre comillas es lo que verá el usuario en pantalla.

¡Ojo! Todo lo que entra con input() es texto (string), aunque pongas números.
edad = input("¿Cuántos años tenés? ")
print(edad + 5)  # ❌ Esto da error
Esto da error porque edad es texto, no número.

✅ Solución: convertí a número con int() o float():
edad = int(input("¿Cuántos años tenés? "))
print(edad + 5)  # Ahora sí suma bien

Salida (print)
Con print() podés mostrar datos en pantalla.
print("Hola, mundo")

Podés mostrar variables también:
nombre = "Gian Luca"
print("Tu nombre es", nombre)

Usar f-strings (formato moderno de texto)
nombre = "Gian"
edad = 20
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
El f al principio indica que vas a meter variables dentro del texto.
Usás { } para insertar las variables.

✅ En resumen:
Función	¿Para qué sirve?
input()	Pedirle algo al usuario (siempre texto)
int()	Convertir texto a número entero
float()	Convertir texto a número decimal
print()	Mostrar cosas por pantalla
f""	Mostrar texto mezclado con variables
"""