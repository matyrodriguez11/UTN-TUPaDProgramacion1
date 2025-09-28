#Inicializamos las listas
titulos = []
ejemplares = []

#Guardamos la opcion
opcion = 0

#Mostramos menu
while opcion != 8:
    print("    Menu principal    \n")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (Préstamo/Devolución)")
    print("8. Salir\n")
    opcion = int(input("Selecciona una opción: "))

    #1. Ingresar títulos
    if opcion == 1:
        cant = int(input("Ingrese la cantidad de titulos que desea ingresar"))
        while cant <= 0:
            print("Cantidad invalida, debe ser mayor o igual a 1")
            cant = int(input("Ingrese la cantidad de titulos que desea ingresar"))
        while cant > 0:
            ingreso = input("Ingrese el titulo del libro")
            titulos.append(ingreso)
            ejemplares.append(0)
            cant -= 1
        
    #2. Ingresar ejemplares
    elif opcion == 2:
        if len(titulos) > 0:
            cant = len(titulos)
            for i in range(cant):
                copias = int(input(f"Ingrese la cantidad de copias para el titulo {titulos[i]}"))
                ejemplares[i] = copias
        else:
            print("Primero debe ingresar a la opcion 1")   

    #3. Mostrar catálogo
    elif opcion == 3:
        if len(titulos) > 0:
            for i in range(len(titulos)):
                print(f"{titulos[i]} || {ejemplares[i]} ejemplares")
        else:
            print("El catalogo esta vacio")

    #4. Consultar disponibilidad
    elif opcion == 4:
        if len(titulos) > 0:
            buscar = input("Ingrese el titulo que desea buscar")
            existe = False
            for i in range(len(titulos)):
                if titulos[i] == buscar:
                    print(f"{titulos[i]} tiene {ejemplares[i]} ejemplares")
                    existe = True
                    break
            if existe == False:
                print("El titulo no se encuentra en el catalogo")
        else:
            print("El catalogo esta vacio")    

    #5. Listar agotados
    elif opcion == 5:
        if len(titulos) > 0:
            existenAgotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"El {titulos[i]} no tiene ejemplares en stock")
                    existenAgotados = True
            if existenAgotados == False:
                print("No hay libros agotados")
        else:
            print("No hay libros en el catálogo.")


    #6. Agregar título
    elif opcion == 6:
        ingreso = input("Por favor, ingrese el titulo del libro que desea ingresar")
        cantidad = int(input("Por favor, ingrese la cantidad de ejemplares del libro recien ingresado"))
        while cantidad < 0:
            print("Cantidad inválida, debe ser mayor o igual a 0")
            cantidad = int(input("Por favor ingrese una cantidad valida"))

        existe = False
        for i in range(len(titulos)):
            if titulos[i] == ingreso:
                existe = True
                break
        if existe == True:
            print("El titulo ya se encuentra en el catalogo")
        else: 
            titulos.append(ingreso)
            ejemplares.append(cantidad)

    #7. Actualizar ejemplares (Préstamo/Devolución)
    elif opcion == 7:
        if len(titulos) > 0:
            actualizar = input("Ingrese el título que desea actualizar")
            existe = False
            pos = -1
            for i in range(len(titulos)):
                if titulos[i] == actualizar:
                existe = True
                pos = i
                break
            if existe == True:
                print("¿Qué desea hacer?")
                print("1. Préstamo")
                print("2. Devolución")
                accion = int(input("Ingrese 1 o 2: "))
                if accion == 1:
                    if ejemplares[pos] > 0:
                        ejemplares[pos] -= 1
                        print(f"Préstamo registrado, quedaron {ejemplares[pos]} ejemplares.")
                    else:
                        print("No hay ejemplares en stock para prestamos")
                elif accion == "2":
                    ejemplares[pos] += 1
                    print(f"Devolución registrada, quedaron en stock {ejemplares[pos]} ejemplares.")
                else:
                    print("Opción inválida.")
        else:
            print("El catalogo esta vacio")

    #8. Salir
    elif opcion == 8:
            print("Finalizando programa")
            break
    
    #Error opcion invalida
    else:
        print("Opcion invalida, recuerde elegir entre el numero 1 y el 8")