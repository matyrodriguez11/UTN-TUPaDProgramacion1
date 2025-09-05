#Ejercicio 1
edad_Usuario = int(input("Por favor, ingrese su edad"))
if (edad_Usuario >= 18):
    print("Es mayor de edad")
else:
    pass

#Ejercicio 2
nota_usuario = int(input("Por favor, ingrese su nota"))
if (nota_usuario >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Por favor, ingrese un numero par"))
resto = numero % 2
if (resto == 0):
    print("Ha ingresado un numero par")
else:
   numero = input("Por favor, ingrese un numero par")

#Ejercicio 4
edad = int(input("Por favor, ingresa tu edad "))
if (edad < 12):
    print("Eres un niño")
elif (18 > edad and edad >= 12):
    print("Eres un adolescente")
elif (30 > edad and edad >= 18):  
    print("Eres un adulto joven")
else:
    print("Eres un adulto")

#Ejercicio 5
contraseña = input("Por favor, ingresa una contraseña de entre 8 y 14 caracteres: ")
cantCaracteres = len(contraseña)
if (cantCaracteres >= 8 and cantCaracteres <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if (media > mediana and mediana > moda):
    print("Sesgo positivo")
elif (media < mediana and mediana < moda):
    print("Sesgo negativo")
elif (media == mediana and mediana == moda):
    print("Sin sesgo")
else:
    pass

#Ejercicio 7
frase = input("Por favor, ingrese una frase o palabra: ")
ultimaLetra = frase[-1]
if (ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u"):
    print(frase + "!")
else:
    print(frase)

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

#Ejercicio 9
magnitud = int(input("Por favor, ingrese en numeros la magnitud de un terremoto: "))
if (magnitud < 3):
    print("Muy leve (imperceptible)")
elif (magnitud >= 3 and magnitud < 4):
    print("Leve (ligeramente perceptible)")
elif (magnitud >= 4 and magnitud < 5):
    print( "Moderado (sentido por personas, pero generalmente no causa daños)")
elif (magnitud >= 5 and magnitud < 6):
    print("Fuerte (puede causar daños en estructuras débiles)")
elif (magnitud >= 6 and magnitud < 7):
    print("Muy Fuerte (puede causar daños significativos)")
elif (magnitud >= 7):
    print("Extremo (puede causar graves daños a gran escala)")
else:
    pass

#Ejercicio 10
hemisferio = input("¿En qué hemisferio te encuentras? (Norte/Sur): ")
mes = int(input("Introduce el número de mes (1-12): "))
dia = int(input("Introduce el día del mes (1-31): "))
hemisferio = hemisferio.lower()


def hemisferioNorte(hemisferio) :
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
    else:
    return "Fecha inválida"
    return estacion_norte if hemisferio == "n" else estacion_sur

def hemisferioSur(hemisferio) :
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
    else:
    return "Fecha inválida"
    return estacion_norte if hemisferio == "n" else estacion_sur    