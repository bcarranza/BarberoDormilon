import os 
barber=[] #1 el barbero
internalBarber=[] #3 sillon
externalBarber=[] #n la calle

while True:
    print("1. Ingreso de cliente")
    print("2. Accionar al barbero")
    print("3. Estado del barbero")
    print("4. Número de clientes en lista de espera dentro de la barbería")
    print("5. Número de clientes en lista de espera fuera  de la barbería")
    print("6. Impresión de la cola")
    print("7. Salir")
    print("Seleccione la opción deseada")
    op=input()
    if(op=="1"): #1. Ingreso de cliente
        print("Bienvenido a la barbería del barbero dormilón")
        print("Ingrese su nombre: ")
        name=input()

        #Ingreso por prioridad
        if(len(barber)==0):
            barber.append(name)
        elif(len(internalBarber)<3):
            internalBarber.append(name)
        else:
            externalBarber.append(name)
        turno=len(barber)+len(internalBarber)+len(externalBarber)
        print("Su turno asignado es: " + str(turno))
    if(op=="2"): #2. Accionar al barbero
        print("Adios estimado: " + str(barber.pop(0)))
        if(len(internalBarber)>0): #Hay cientes en el sillon?
            barber.append(internalBarber.pop(0)) # El barbero toma una cliente
            print("Bienvendo: " + str(barber[0]))
            if(len(internalBarber)<3 and len(externalBarber)>0): #Significa que si existe cliente en la calle, lo va ingresar al sillon.
                internalBarber.append(externalBarber.pop(0))
        else:
            print("Que bueno, ya no hay client... zzzzzzzzzzzz");
    if(op=="3"): # 3. Estado del barbero
        if(len(barber)>0):
            print("El barbero esta atendiendo a cliente: " + str(barber[0]))
        else:
            print("Shhhhhhhhhhhhhhhhhhhh el barbero esta durmiendo, no lo molestes!!!")
    
    if(op=="4"): #4. Número de clientes en lista de espera dentro de la barbería
        print("Contamos con " + str(len(internalBarber)+1) + " clientes dentro de la barberia")
    if(op=="5"):  #5. Número de clientes en lista de espera fuera  de la barbería
        print("Contamos con " + str(len(externalBarber)) + " clientes fuera de la barberia")
    if(op=="6"): #6. Impresión de la cola
        totalArray=[]
        if(len(barber)>0):
            totalArray=barber
        if(len(internalBarber)>0):
            totalArray=totalArray + internalBarber
        if(len(externalBarber)>0):
            totalArray=totalArray + externalBarber
        print("Imprimiendo total de la cola")
        print("----------------------------")
        for v in totalArray:
            print(v)
        print("----------------------------")
    if(op=="7"):
        print("Hasta Luego")
        break
    input("Presione enter para continuar")
    os.system('cls')    




