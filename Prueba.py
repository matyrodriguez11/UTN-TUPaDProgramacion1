#Ejercicio 8
nombre = input("Por favor, ingrese su nombre: ")
opcion = int(input("""Por favor, elija una opcion ingresando 1, 2 o 3: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro
"""))
if (opcion == 1):
    print(nombre.upper())
elif (opcion == 2):
    print(nombre.lower())
elif (opcion == 3):
    print(nombre.title())
else:
    pass
