
#Realizar un programa que solicite al usuario un número indeterminado de números (mientras se tecleen números que no sean cero). Al salir el programa debe dar en pantalla el total de números dados y la suma de ellos.

numeros_insertados = 0
suma_numeros = 0

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    numeros_insertados += 1
    suma_numeros += numero

print("Total de números dados:", numeros_insertados)
print("Suma de los números:", suma_numeros)
