"""
-Aritmeticos
Los operadores aritméticos sirven para hacer cuentas en Python, como sumar, restar o multiplicar. Acá te los explico uno por uno:
Suma (+): suma dos valores.
Ejemplo: 10 + 3 da 13.

Resta (-): resta el segundo valor al primero.
Ejemplo: 10 - 3 da 7.

Multiplicación (*): multiplica los dos valores.
Ejemplo: 10 * 3 da 30.

División (/): divide el primer valor por el segundo y da un número con decimales.
Ejemplo: 10 / 3 da 3.333....

División entera (//): hace la división pero solo te da la parte entera, sin decimales.
Ejemplo: 10 // 3 da 3.

Módulo (%): da el resto de una división.
Ejemplo: 10 % 3 da 1 (porque 3 entra 3 veces en 10, y sobra 1).

Exponenciación ()**: eleva un número a la potencia del otro.
Ejemplo: 10 ** 3 es lo mismo que 10 x 10 x 10, y da 1000.

-De comparación
Los operadores de comparación sirven para comparar dos valores. Siempre te devuelven True (verdadero) o False (falso), según el resultado de la comparación.

Igual a (==): da True si los dos valores son exactamente iguales.
Ejemplo: 10 == 3 da False.

Distinto de (!=): da True si los valores son diferentes.
Ejemplo: 10 != 3 da True.

Mayor que (>): da True si el primer valor es más grande que el segundo.
Ejemplo: 10 > 3 da True.

Menor que (<): da True si el primer valor es más chico que el segundo.
Ejemplo: 10 < 3 da False.

Mayor o igual que (>=): da True si el primer valor es más grande o igual al segundo.
Ejemplo: 10 >= 3 da True.

Menor o igual que (<=): da True si el primer valor es más chico o igual al segundo.
Ejemplo: 10 <= 3 da False.

Estos operadores se usan mucho en decisiones (if) o en bucles (while, for).

-Lógicos
Los operadores lógicos sirven para juntar condiciones y ver si algo es verdadero o falso.

AND (and): devuelve True solo si las dos condiciones son verdaderas.
Ejemplo: (10 > 5) and (3 < 5) da True, porque las dos son verdaderas.

OR (or): devuelve True si al menos una condición es verdadera.
Ejemplo: (10 > 15) or (3 < 5) da True, porque una de las dos es verdadera.

NOT (not): invierte el resultado. Si algo es True, lo convierte en False, y si es False, lo convierte en True.
Ejemplo: not (10 > 5) da False, porque 10 > 5 es verdadero, y el not lo invierte.

Usás estos operadores cuando querés que algo pase solo si se cumplen ciertas condiciones.
Por ejemplo: si una persona es mayor de edad y tiene entrada, puede entrar.
Eso se escribiría como:
if edad >= 18 and tiene_entrada:
"""