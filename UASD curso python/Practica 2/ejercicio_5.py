#5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100

# Define límites y cantidad de billetes disponibles
limite_retiro_abc = 10000
limite_transaccion_abc = 2000
billetes_disponibles = {'1000': 9, '500': 19, '100': 99}

# Solicita banco y monto a retirar al usuario
banco = input("Ingrese el nombre del banco: ")
monto_a_retirar = float(input("Ingrese el monto a retirar: "))

# Verifica el límite de transacción
if banco.upper() == "ABC" and monto_a_retirar > limite_transaccion_abc:
    print(f"El monto solicitado excede el límite de transacción de {limite_transaccion_abc} pesos.")
elif banco.upper() != "ABC" and monto_a_retirar > limite_retiro_abc:
    print(f"El monto solicitado excede el límite de retiro de {limite_retiro_abc} pesos.")
else:
    # Calcula la cantidad de billetes a dispensar
    monto_total_retirado = monto_a_retirar 
    billetes_dispensados = {'1000': 0, '500': 0, '100': 0}

    for denominacion in billetes_dispensados:
        cantidad_billetes = min(billetes_disponibles[denominacion], monto_a_retirar // int(denominacion))
        billetes_dispensados[denominacion] = cantidad_billetes
        monto_a_retirar -= cantidad_billetes * int(denominacion)
        billetes_disponibles[denominacion] -= cantidad_billetes

    # Verificar si el monto solicitado no puede ser dispensado completamente
    if monto_a_retirar > 0:
        print("El monto solicitado no puede ser dispensado completamente.")
    else:
        # Muestra la distribución de billetes
        print("Billetes dispensados:")
        for denominacion, cantidad in billetes_dispensados.items():
            if cantidad > 0:
                print(f"{cantidad} billete(s) de {denominacion} pesos.")
print("usted ha retirado RD$"+str(monto_total_retirado)+" del banco "+str(banco)+".")