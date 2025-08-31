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
