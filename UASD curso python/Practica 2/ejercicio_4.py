#Realizar un programa que reciba por teclado el sueldo de un empleado y le aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

print("          Bienvenido al sistema de cálculo de \n          impuestos de la República Dominicana \n")
def calcular_impuesto_sobre_renta_mensual(salario_mensual):
    ingreso_anual = salario_mensual * 12

    if ingreso_anual <= 416220.00:
        impuesto = 0
    elif ingreso_anual <= 624329.00:
        excedente = ingreso_anual - 416220.00
        impuesto = 0.15 * excedente / 12
    elif ingreso_anual <= 867123.00:
        excedente = ingreso_anual - 624329.01
        impuesto = (31216.00 + 0.20 * excedente) / 12
    else:
        excedente = ingreso_anual - 867123.01
        impuesto = (79776.00 + 0.25 * excedente) / 12

    return impuesto

# Solicita el salario mensual del empleado
try:
    salario_mensual = float(input("Ingrese el salario mensual del empleado: "))
    impuesto_calculado = calcular_impuesto_sobre_renta_mensual(salario_mensual)
    print(f"\nEl impuesto sobre la renta mensual a pagar es: RD${impuesto_calculado}\n")
except ValueError:
    print("Por favor, ingrese un valor numérico para el salario mensual.")


try:
    porcentaje_afp = 2.87 / 100  # Convertir el porcentaje a decimal
    impuesto_afp = salario_mensual * porcentaje_afp

    print(f"El impuesto por AFP a pagar es: RD${impuesto_afp:.2f}\n")
except ValueError:
    print("Por favor, ingrese un valor numérico para el salario mensual.")

try:
    porcentaje_ars = 3.04 / 100  # Convertir el porcentaje a decimal
    impuesto_ars = salario_mensual * porcentaje_ars

    print(f"El impuesto por ARS a pagar es: RD${impuesto_ars:.2f}")
except ValueError:
    print("Por favor, ingrese un valor numérico para el salario mensual.")

