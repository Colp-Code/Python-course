#casefold() Combierte el texto en minusculas
"""
Metodo casefold() en Python
    Ejemplo
Escribe la cadena de texto en minusculas 
"""
texto = "Hola, Como Estan Amigos"
q = texto.casefold()#"hola, como estan amigos"
print(q)
"""
Definicion y uso
El metodo casefold() devuelve una cadena de texto donde todos los caracteres estan en minusculas.

Este metodo es similar al metodo lower() pero el metodo casefold() es fuerte, mas agresivo, significa que
convertira mas caracteres en minusculas, y encontrara mas caracteres cuando comparas dos cadenas de texto
y ambas se convertiran usando el metodo casefold()

Syntaxis
texto.casefold()
Parametros
|No tiene parametros|
"""