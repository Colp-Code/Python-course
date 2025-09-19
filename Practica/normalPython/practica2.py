# Pide un número y muestra si es par o impar.

numero = int(input('Escribe un numero'))

resultado = numero % 2

if numero % 2 == 0:
    print("este numero es par")
else:
    print("este numero es impar")
