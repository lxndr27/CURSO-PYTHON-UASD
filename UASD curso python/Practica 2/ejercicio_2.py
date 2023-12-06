'''Realizar un programa que presente un menú con las siguientes opciones
1- Convertir grados a Celsius a Fahrenheit
2- Convertir dólar a pesos
3- Convertir metros a pies
4- Salir
Cada vez que finalice una de estas acciones debe regresar al menú. El programa
solo finalizará cuando el usuario elija la opción salir.'''

while True:
    print("Menú:")
    print("1- Convertir Celsius a Fahrenheit")
    print("2- Convertir Dólar a Pesos")
    print("3- Convertir Metros a Pies")
    print("4- Salir")

    opcion = int(input("Ingresa tu elección: "))

    if opcion == 1:
        print("Seleccionaste la opción 1")
    elif opcion == 2:
        print("Seleccionaste la opción 2")
    elif opcion == 3:
        print("Seleccionaste la opción 3")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, inténtalo de nuevo.")

