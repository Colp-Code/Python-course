print("Hola, ¿qué quieres calcular? Aquí te dejo las opciones:")
print("1: A partir del porcentaje anual")
print("2: A partir del porcentaje mensual")
print("3: A partir del porcentaje diario")

elec = int(input("¿Cuál opción quieres?: "))
porcentaje = float(input(f"¿Qué porcentaje quieres calcular?: "))

if elec == 1:  # De anual a mensual y diario
    print("Opción: Cálculo desde el porcentaje anual")
    mes = (1 + porcentaje/100)**(1/12) - 1
    print(f"El porcentaje mensual es: {mes * 100:.6f}%")
    dia = (1 + porcentaje/100)**(1/365) - 1
    print(f"El porcentaje diario es: {dia * 100:.6f}%")

elif elec == 2:  # De mensual a anual y diario
    print("Opción: Cálculo desde el porcentaje mensual")
    año = (1 + porcentaje/100) ** 12 - 1
    print(f"El porcentaje anual es: {año * 100:.6f}%")
    dia = (1 + porcentaje/100) ** (1/30) - 1
    print(f"El porcentaje diario es: {dia * 100:.6f}%")

elif elec == 3:  # De diario a anual y mensual
    print("Opción: Cálculo desde el porcentaje diario")
    año = (1 + porcentaje/100) ** 365 - 1
    print(f"El porcentaje anual es: {año * 100:.6f}%")
    mes = (1 + porcentaje/100) ** 30 - 1
    print(f"El porcentaje mensual es: {mes * 100:.6f}%")

else:
    print("Opción no válida. Debes elegir 1, 2 o 3.")