#Ejercicio 1
for i in range(0,101):
    print(i)

#Ejercicio 2
numero = int(input("Por favor ingrese un numero entero: "))
contador = 0
while numero > 10:
    numero = numero // 10 
    contador += 1
print(f"El numero tiene {contador} digitos")

#Ejercicio 3
inicial = int(input("Por favor ingresa un numero entero inicial: "))
final = int(input("Por favor ingresa un numero entero final: "))
sumatoria = 0
for i in range ((inicial+1), (final)):
    sumatoria += i
print(sumatoria)

#Ejercicio 4
total = 0    
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")

#Ejercicio 5
import random
numeroAleatorio = random.randint(0, 9)
intentos = 0
numero = 10
print("Adivina en que numero del 0 al 9 estoy pensando")
while (numeroAleatorio != numero):
    intentos += 1
    numero = int(input("Ingresa el numero que crees que es: "))
print(f"Necesitaste {intentos} intentos para acertar")

#Ejercicio 6
for i in range(100,0, -2):
    print (i)

#Ejercicio 7
final = int(input("Por favor ingresa un numero: "))
sumatoria = 0
for i in range ((0), (final+1)):
    sumatoria += i
print(sumatoria)

#Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese 100 números enteros:")

for i in range(100):
    num = int(input(f"Número {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#Ejercicio 9
print(f"Ingrese 100 números enteros:")
sumatoria = 0
promedio = 0

for i in range(100):
    num = int(input(f"Número {i+1}: "))
    sumatoria += num

promedio = sumatoria / 100

print("La media de los 100 numeros es", promedio)

#Ejercicio 10
numero = int(input("Ingresa un número: "))
numeroInvertido = 0

while numero > 0:
    digito = numero % 10
    numeroInvertido = numeroInvertido * 10 + digito
    numero //= 10

print(numeroInvertido)