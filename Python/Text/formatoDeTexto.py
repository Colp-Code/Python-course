"""
Formatos de cadenas de texto en Python

Formatos de texto
Como aprendimos en el capitulo de variables en Python, no podemos combinar cadenas de texto y numeros como esto:
"""

# edad = 36
# txt = "Mi nombre es jimmy, y tengo " + edad
# print(txt)   Esto da error

"""
Pero podemos combinar las cadenas de texto con numeros usando el metodo format()

F-String fueron introsducidos en la version 3.6 de Python, y es ahora la preferencia perfecta de formatear una cadena

Para espesificar una cadena de texto como un f-String somplemente pon f al frente de la cadena de texto y agrega corchetes como marcadores de posicion de variables y otras operaciones.

    Ejemplo
crear un f-String
"""
edad = 36
txt = f"Mi nombre es jimmy y tengo {edad}"
print(txt)

"""
Marcadores y modificadores

Un marcador puede contener variables, operaciones, funciones, y modificar el valor del formato

    Ejemplo
añadir un marcador por el precio del valor
"""

precio = 30
txt = f"El precio es {precio} dolares"
print(txt)

"""
Un marcador puede incluir un modifidcarod de formato 

Un modificador se incluye añadiendo doble punto: seguido por un tipo de fortamo valido como .2f que significa un coma fija
    Ejemplo
Mostrar el precio con 2 decimales:
"""

precio = 59
txt = f"el precio es {precio:.2f} dolares"
print(txt)

"""
Un marcador puede contener codigo de Python, operaciones matematicas:
    Ejemplo
realize una operacion matematica en un marcador de pisicion y devuelve el resultado:
"""

txt = f"El precio es {20 +18} dolares"
print(txt)