#Hacer un programa que genere las tablas de multiplicar de los números múltiplos de 5 que hay entre 1 y 1000
for num in range(5, 1001, 5):
    print(f"Tabla de multiplicar de {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")
    print("\n")

