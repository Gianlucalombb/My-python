"""
¿Qué es un diccionario?
Un diccionario es como una lista, pero en vez de usar números (índices) para acceder a los datos, usás claves (palabras, números, etc.).

Cada elemento del diccionario tiene dos partes:

una clave (como un nombre),

y un valor (lo que le corresponde a esa clave).

Se escribe así:

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
🔍 Cómo acceder a los valores
Para ver lo que hay dentro de una clave, usás corchetes con el nombre de la clave:

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
También podés usar get():

print(persona.get("ciudad"))       # Imprime "Madrid"
print(persona.get("altura"))       # No existe → imprime None
print(persona.get("altura", 0))    # No existe → imprime 0 (valor por defecto)
🔧 Métodos útiles de los diccionarios
keys() → muestra todas las claves.

values() → muestra todos los valores.

items() → muestra todo: claves y valores juntos.

update({...}) → agrega o cambia datos en el diccionario.

Ejemplo:
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())     # dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values())   # dict_values(['Juan', 25, 'Madrid'])
print(persona.items())    # dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])

persona.update({"profesion": "Ingeniero"})
print(persona)
# {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
En resumen:
Los diccionarios guardan pares de clave y valor.

Se escriben con llaves {}.

Las claves son únicas y te sirven para acceder directamente al valor.

Se pueden modificar, agregar o quitar datos. Por eso se dice que son mutables
"""
"""
Ejercicio 1 - Datos personales
Escribí un programa que:

Cree un diccionario llamado persona con estos datos:

nombre: "Lucas"

edad: 30

ciudad: "Rosario"

Imprima el nombre, la edad y la ciudad usando las claves del diccionario.

datos_personales = {
    "nombre": "Lucas",
    "edad": 30,
    "ciudad": "Rosario"
}

print(datos_personales["nombre"])
print(datos_personales["edad"])
print(datos_personales["ciudad"])
"""

"""
Ejercicio 2: Modificar y actualizar un diccionario

Crea un diccionario llamado persona con las claves: "nombre", "edad" y "ciudad", y asigna valores que quieras.

Cambia el valor de la clave "edad" a otro número.

Agrega una nueva clave "profesion" con un valor que te guste.

Imprime el diccionario completo para ver los cambios.




persona = {
    "nombre": "Gian",
    "edad": 20,
    "ciudad": "caba"
}

persona.update({"edad": 21})
persona.update({"profesion": "Ingeniero"})

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona["profesion"])
"""
