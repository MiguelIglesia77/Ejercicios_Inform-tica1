Nm=int(input("Ingrese el número de mediciones:"))
Promedio=0
Mediciones=0
Contador=0
while Contador<Nm:
    Mediciones=int(input("Ingrese el valor de la temperatura en °C"))
    Promedio+=Mediciones
    Contador+=1
    if Mediciones >30:
        print("Alerta mayor a 30°")
    elif Mediciones<15:
        print("Alerta menor a 15°")
    if Nm==Contador:
        print("El promedio es {x}." .format(x=(Promedio/Nm)))