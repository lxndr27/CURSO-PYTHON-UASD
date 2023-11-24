#Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F.

calificaciones = [90, 95, 77, 92]

promedio = sum(calificaciones) / len(calificaciones)

if promedio >= 90:
    print('Su calificacion final es una A')
elif promedio >= 80:
    print('Su calificacion final es una B')
elif promedio >= 70:
    print('Su calificacion final es una C')
elif promedio >= 60:
    print('Su calificacion final es una D')
elif promedio >= 50:
    print('Su calificacion final es una E')
else:
    print('Su calificacion final es una F')
