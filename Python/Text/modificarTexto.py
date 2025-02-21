"""
Modificar texto en Python
Python tiene un congunto de metodos incorporados que puedes usar con las cadenas de texto.

Mayusculas
    Ejemplo
El metodo upper() devuelve una cadena de texto en mayusculas:
"""

q = "Hola mundo!"
print(q.upper())

"""
Munusculas
    Ejemplo
El metodo lower() devuelve una cadena de texto en minusculas:
"""

w = "HOLA MUNDO!"
print(w.lower())

"""
Remover espacios en blanco 

Los espacio en blanco son el espacio que esta entes y/o despues de el texto actual, y esto muy a menudo querras quitar estos espacios 
    Ejemplo
El metodo strip() remueve cualquier espacio en blanco de el inicio y el final:
"""

e = " Hola mundo! "
print(e.strip())

"""
Remplasar cadena de texto
    Ejemplo
El metodo replace() remplasa una cadena de texto con otra cadea de texto:
"""

r = "Hola mundo!"
print(r.replace("H", "P"))

"""
Dividir cadena de texto

El metodo split() devuelve una lista donde el texto entre el separador espesificado se convierte en una lista de objetos.
    Ejemplo
El metodo split() divide el texto en sub-textos si encuentra la instancia del separador:
"""

t = "Hola mundo!"
print(t.split(" "))