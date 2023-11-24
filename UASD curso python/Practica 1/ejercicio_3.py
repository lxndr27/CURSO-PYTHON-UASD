#Evalúe si un número es par o impar y muestre en la consola el mensaje.

#En esta primera variante el valor de la variable se lo estoy dando directamente en el codigo.
numero = 123
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

#En esta segunda variante el valor de la variable lo ingreso por teclado. O sea que el valor de la variable lo ingresa el usuario.
numero = int(input("Ingrese un numero: ")) 
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
