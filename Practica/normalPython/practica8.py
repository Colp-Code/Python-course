numero = int(input(f'Ingresa un numero: '))
x = 0
for i in range(1,numero):
    if numero % i == 0:
        x += i
        print(x)
        if x == numero:
            print(f'El numero {x} es un numero perfecto')

if x != numero:
            print(f'El numero {numero} no es un numero perfecto')