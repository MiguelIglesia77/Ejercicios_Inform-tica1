LD = []
LC = []
CD = 0
CC = 0

print("Bienvenido al programa de la clínica veterinaria UdeA\n".upper().center(90))
while True:
    Menú = int(input("""Ingrese:\n
                     1. Ingresar nuevo paciente.
                     2. Ver cantidad de pacientes.
                     3. Ver el promedio de edades.
                     4. Cantidad de pacientes en estado crítico y grave.
                     5. Ver información del paciente.
                     6. Ver listado de todos los pacientes.
                     7. Salir\n"""))
    if Menú==1:
        mas = []
        mas.append(input("Nombre de la mascota:\n"))
        especie = int(input("Ingrese: \n0- Si es perro. \n1- Si es gato. \n"))
        if especie==0:
            mas.append("Perro")
        else:
            mas.append("Gato")
        mas.append(int(input("Ingrese la edad de la mascota: \n")))
        estado = int(input("Ingresar: \n0- Si es grave. \n1- Si es crítico. \n"))
        if estado==0:
            mas.append("Grave")
        else: 
            mas.append("Crítico")
        if especie==0:
            CD+=1
            codigo = f"Caninos{CD:03d}"
            mas.append(codigo)
            LD.append(mas)
        elif especie==1:
            CC+=1
            codigo = f"Felinos{CC:03d}"
            mas.append(codigo)
            LC.append(mas)
        else:
            print("Por favor ingrese un número válido, 1 ó 0")
            continue
    elif Menú==2:
        Tt=int(input("Ingrese para visualizar: \n1-Cantidad de perros. \n2-Cantidad de gatos. \n3-Total de pacientes. \n"))
        if Tt==1:
            print("\nHay %d perros en el sistema \n" % len(LD))
        elif Tt==2:
            print("\nHay %d gatos en el sistema \n" % len(LC))
        elif Tt==3:
            print("\nHay %d animales en el sistema \n" % (len(LD)+len(LC)))
        else:
            print("Ingrese una opción válida: 1, 2 o 3.")
            continue
    elif Menú==3:
        ages= []
        for i in LC:
            ages.append(i[2])
        for i in LD:
            ages.append(i[2])
        print (f"El promedio de edad es: {sum(ages)/len(ages):.2f}")
    elif Menú==4:
        C_graves=0
        C_críticos=0
        for i in LC:
            if i[3]=="Grave":
                C_graves+=1
            else:
                C_críticos+=1
        for i in LD:
            if i[3]=="Grave":
                C_graves+=1
            else:
                C_críticos+=1
        print(f"Hay {C_graves} pacientes graves y {C_críticos} pacientes críticos en el sistema.")
    elif Menú==5:
        cod=(input("Ingrese el código del animal que desea buscar")).capitalize()
        if cod.startswith("Fe"):
            for i in LC:
                if i[4]==cod:
                    print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: i[2]\n Estado: {i[3]}\nCodigo {i[4]}")
        elif cod.startswith("Ca"):
            for i in LD:
                if i[4]==cod:
                    print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: i[2]\n Estado: {i[3]}\nCodigo {i[4]}")
    elif Menú==6:
        Lt = LD+LC
        for i in Lt:
            print(f"Nombre: {i[0]} \nTipo : {i[1]}\n Edad: {i[2]}\n Estado: {i[3]}\nCodigo {i[4]}")
    elif Menú==7:
        fallos=0
        while fallos<3:
            SM = input("\n1-Aceptar. \n2-Rechazar.")
            if SM==("1"):
                break
            elif SM==("2"):
                break
            else:
                fallos+=1
                print("Ingrese una opción que sea válida")
        if SM ==("1"):
            break
        elif SM !=1:
            continue