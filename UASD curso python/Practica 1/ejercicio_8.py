#Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual(Amortizar mediante el sistema francés)

monto = float(input("Ingrese el monto del préstamo: "))
cuotas = int(input("Ingrese la cantidad de cuotas: "))
interes_anual = float(input("Ingrese el porcentaje de interés anual: "))

interes_mensual = interes_anual / 12 / 100
cuota_mensual = monto * (interes_mensual * (1 + interes_mensual) ** cuotas) / ((1 + interes_mensual) ** cuotas - 1)

print("La cuota mensual es:", cuota_mensual)
