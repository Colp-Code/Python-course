"""
<h1>Espesificar un tipo de variable</h2>

Puede haber un momento cuando tu nesecitas un tipo espesifico de dato en una variable. Esto se hace con casting.
Python es un lenguaje orientado a objetos y como tal usa las clases para definir los tipos de datos, incluyendo los tipos primitivos

La conversión en Python es por lo tanto usado para hacer funciones constructoras.

-   int() Contruir un numero entero a un numero entero literal, de un numero flotante a numero entero (esto se hace quietando los decimales)
    o una cadena de texto(siempre que el texto represente un numero entero)

-   float() La contrucion de un numero entero a un numero flotante, de una cadena de texto a un numero flotante(siempre que el texto represente un numero flotante o un numero entero)

-   str() Contruir un texto a partir de varios tipos de datos incluyendo textos, numeros enteros y numeros flotantes

"""
# ------------
#   Ejemplo con la funcion int()
# ------------

q = int(1)
w = int(2.8)
e = int("3")
print(q,w,e)

# ------------
#   Ejemplo con la funcion float()
# ------------

r = float(1)
