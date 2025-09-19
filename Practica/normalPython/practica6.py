print("Hola, que quieres calcular aqui te dejo las opciones \n 1: año \n 2: mes \n 3: dia")

elec = int(input(f"Cual quieres?"))
porcentaje = float(input(f"que porcentaje quieres?"))

if elec == 1:
    print("opcion año")
    mes = (1 + porcentaje/100)**(1/12) -1
    print(f'El porcentaje del mes es: {mes * 100:.6f}%')
    dia = (1 + porcentaje/100)**(1/365) -1
    print(f'El porcentaje del dia es: {dia * 100:.6f}%')
elif elec == 2:
    año = (porcentaje/100 + 1)** 12 -1
    print(f'El porcentaje del año es: {año * 100:.6f}%')
    dia = (porcentaje/100 + 1)**(1/30)-1
    print(f'El porcentaje del dia es: {dia * 100:.6f}%')
elif elec == 3:
    año = (1 + porcentaje/100)** 365 -1
    print(f'El porcentaje del año es: {año * 100:.6f}%')
    mes = (1 + porcentaje/100)** 30 -1
    print(f'El porcentaje del mes es: {mes * 100:.6f}%')