# capitalize() combierte la primera letra en mayusculas
"""
Metodo de cadena de texto capitalize() en Python

    Ejemplo
Comvierte la primera letra en mayusculas 
"""
texto = "hola"
q = texto.capitalize()
print(q)#"Hola"
Texto = "hola, bienvenidos a mi casa"
w = Texto.capitalize()
print(w)#"Hola, bienvenidos a mi casa"
"""
Definicion y uso
El metodo capitalize() devuelve una cadena de texto donde el primer caracter es mayusculas y el resto esta en minusculas 

Syntaxis
|texto.capitalize()|
Parametros
|No hay parametros|

Mas ejemplos
    Ejemplo
El primer caracter es convertido en mayusculas y el resto son convertidos en minusculas:
"""
texto2 = "python es ¡MUY BUENO!"
e = texto2.capitalize()
print(e)#"Python es ¡muy bueno!"
"""
    Ejemplo
Mira lo que pasa si el primer caracter es un numero:
"""
texto3 = "20 años, ya estas viejo :)"
r = texto3.capitalize()#"20 años, ya estas viejo :)"
print(r)