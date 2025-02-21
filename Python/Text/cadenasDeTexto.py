"""
<h1>Cadena de texto</h1>

Las cadenas de texto en python estan rodeadas o bien de comillas simples o comillas dobles

'hola' es lo mismo que "hola"

Puedes mostrar una cadena de texto con la funcion print()

"""
#ejemplo

print("hola")
print('hola')

# Citaciones dento de citaciones

# Puedes usar una cita dentro de una cadena de texto Simepre y cuando no coinsida con las comillas alrededor del texto

# Ejemplo

print("Como estas pa'")
print("El se llama 'Jimmy'")
print('El se llama "Mono"')

# Asignar texto a una variable

# Asignar un texto a una variable se realiza con el nombre de la variable seguido de un signo igual y el texto

# Ejemplo 

q = "hola"
print(q)

#   Multiples cadenas de texto

# tu puedes asignar multiplas cadenas de texto a una variable usando tres comillas 

w = """Hola muchacho como estas,
bien la verdad y tu vomo estas,
estoy mirando como mejoro mi estado economico,
a eso esta bien."""
e = '''Hola muchacho como estas,
bien la verdad y tu vomo estas,
estoy mirando como mejoro mi estado economico,
a eso esta bien.'''
print(w,e)

#   Las cadenas de texto son arrays 

"""
Como muchos otros lenguajes populares, las cadenas de texto en python son arrays de
bytes representado por caracteres unicode.

Sin embargo, python no tiene un tipo de dato, un simple caracter es un simple cadena de texto con longitud de 1
Los conchetes pueden usarse para aceder a los elementos de un cadena de texto

"""
#   ejemplo
# obten el caracter de la posicion 1 (recuerda que el primer caracter esta en la pocision 0):

r = "hola mundo!"
print(r[1])

#<h2>Bucle a traves de una cadena de texto</h2>
#   Ya que una cadena de texto es un array, podemos hacer un bucle a traves de los caracteres en una cadena de texto con el bucle for

#   Ejemplo
# bucle a traves de las letras de la palabra "banano"

for t in "banano":
    print(t)

# Tamaño de una cadena de texto

# para obtener la longitud de una cadena de texto, usaremos la funcion len()

#   Ejemplo
# La funcion len() devuelve el tamaño de la cadena de texto

y = "Hola mundo!"
print(len(y))

# comprobar cadena de texto
# para comparar si cierta frase o un caracter esta presente es una cadena de texto, podemos usar la palabra clave in.

#   Ejemplo
# Comprobrar si "gratis" esta presente en el siguente texto:

txt = "Las mejores cosas en esta vida son gratis"
print("gratis" in txt)

# Usalo en una declaracion if
#   Ejemplo
# inprime solo si "gratis" esta presente

txt2 = "Las mejores cosas en esta vida son gratis"
if "gratis" in txt2:
    print("si, la palabra 'gratis' esta presente.")

#   Comprobrar si no
# Para comprobar si cierta frase o caracter no esta presente en una cadena de texto, podemos usar la palabrta clave not in.
#   Ejemplo
# Comprobar si "caro" no esta presente en el siguiente texto:

txt3 = "Las mejores cosas en esta vida son gratis"
print("caro" not in txt3)

#   Usalo en una declaracion if
#   Ejemplo
# Imprime solo si "caro" no esta presente:

if "caro" not in txt3:
    print("No, 'caro'  no esta en esta cadena de texto")

