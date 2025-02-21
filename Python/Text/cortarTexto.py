"""
    Cortar texto en Python

Cortar
puedes devolver un rango de caracteres por usar el "slice syntax".

Espesifique el indice inicial y el indice final, separado de dos punto, para devolver la parte de la cadeta de texto.

    Ejemplo
Obtener los caracteres de la posicion 2 a la posicion 5(no incluida):

"""
q = "Hola mundo!"
print(q[1:5])

"""
    Rebanar desde el inicio
Al omitir el indice inicial, el rango iniciara desde el primer caracter:
    Ejemplo
Obterner los caracteres desde el inicio hasta las pisicion 5(No incluida):
"""

w = "Hola mundo!"
print(w[:5])

"""
Cortar hasta el final

Omitiendo el indice del final, el rango se ira hasta el final
    Ejemplo
Obtener los caracteres desde la posicion 2 y todo hasta el final 
"""

e = "Hola mundo!"
print(e[2:])

"""
Indexacion negativa

Usa la indexacion negativa para iniciar el corte desde el final de la cadena de texto
    Ejemplo
Obtener los caracteres:
desde: "u" in "mundo"(posición -3)
a, pero no incluir: "d" en mundo(posición -2)
"""

r = "hola mundo!"
print(r[-6:-3])

