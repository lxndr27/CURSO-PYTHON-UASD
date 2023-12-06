#5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100

billetes_1000 = 9
billetes_500 = 19
billetes_100 = 99

limite_retiro_abc = 10000
limite_transaccion_abc = 2000

limite_retiro = limite_retiro_abc
limite_transaccion = limite_transaccion_abc

while True:
    banco = input("Ingrese el nombre del banco: ")
    monto_a_retirar = int(input("Ingrese el monto a retirar: "))

    if monto_a_retirar > limite_retiro:
        print("El monto solicitado excede el límite de retiro.")
    elif monto_a_retirar > limite_transaccion:
        print("El monto solicitado excede el límite de transacción por transacción.")
    else:
        billetes_dispensados_1000 = min(billetes_1000, monto_a_retirar // 1000)
        monto_a_retirar -= billetes_dispensados_1000 * 1000

        billetes_dispensados_500 = min(billetes_500, monto_a_retirar // 500)
        monto_a_retirar -= billetes_dispensados_500 * 500

        billetes_dispensados_100 = min(billetes_100, monto_a_retirar // 100)
        monto_a_retirar -= billetes_dispensados_100 * 100

        if monto_a_retirar == 0:
            print("\nMonto dispensado:")
            print(f"Billetes de 1000: {billetes_dispensados_1000}")
            print(f"Billetes de 500: {billetes_dispensados_500}")
            print(f"Billetes de 100: {billetes_dispensados_100}")

            limite_retiro -= sum([billetes_dispensados_1000 * 1000, billetes_dispensados_500 * 500, billetes_dispensados_100 * 100])
        else:
            print("\nNo se puede dispensar el monto solicitado debido a la falta de billetes.")

    continuar = input("\n¿Desea realizar otra transacción? (Sí/No): ")
    if continuar.lower() != 'si':
        break

print(f"\nLímite de retiro restante: {limite_retiro}")
