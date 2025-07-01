"""
¿Qué es un archivo en Python?
Es simplemente un archivo de texto (como .txt) que tu programa puede leer o modificar.

1. Leer un archivo (modo "r")
Querés ver qué tiene un archivo .txt.
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
"r" significa modo lectura
read() lee todo el contenido del archivo
close() cierra el archivo (¡es obligatorio!)

✅ Mejor forma: with open()
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

Lo bueno de with es que cierra el archivo solo, aunque algo falle.

2. Escribir en un archivo (modo "w")
Si querés escribir texto dentro de un archivo:
archivo = open("datos.txt", "w")
archivo.write("Hola, Gian!")
archivo.close()
"w" significa modo escritura
Si el archivo no existe, lo crea
Si ya existe, borra todo lo anterior y lo reemplaza

3. Agregar texto sin borrar (modo "a")
archivo = open("datos.txt", "a")
archivo.write("\nNueva línea de texto")
archivo.close()
"a" es modo añadir (append)
No borra lo anterior, agrega al final

Resumen rápido
Modo	Significado	¿Borra contenido?	¿Crea archivo si no existe?
"r"	Leer	❌ No	❌ No
"w"	Escribir desde cero	✅ Sí	✅ Sí
"a"	Agregar al final	❌ No	✅ Sí

Consejos
Siempre cerrá los archivos (o usá with)

Usá try-except si el archivo puede no existir

Siempre indicá el nombre del archivo con la ruta correcta
"""