print("Escribe un numero para mirar si es primo o no")
numeroIn = int(input(f'¿Que numero escojes?: '))

for operacion in range(2,numeroIn):
    x = numeroIn % operacion
    if x == 0:
        print(f'El numero {numeroIn} no es primo')
        break