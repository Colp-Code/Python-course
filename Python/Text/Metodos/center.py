#center() Devuelve una cadena de texto centrada
"""
El metodo center() en Python
    Ejemplo
Improme la palabra "Empanada" ocupando el espacio de 20 caracteres con "Empanada" en el centro:
"""
texto = "Empanada"
q = texto.center(20)
print(q)

"""
Definicion y uso

El metodo center() Alineara al centro el texto, usando un caracter especial (El estacio esta por defecto)
como caracter de relleno

Syntaxis
texto.center(longitud, caracter)
Parametros
Parametro: length Requiere la longitud de la cadena devuelta 
Parametro: character(opcional) El caracter para rellenar el espacio perdido en cada lugar. Lo predeterminado es " "(Espacio)

Mas ejemplos
    Ejemplo
Usando la letra "O" como el caracter de relleno
"""
texto2 = "Empanada"
w = texto2.center(20,"O")
print(w)#"OOOOOOEmpanadaOOOOOO"
