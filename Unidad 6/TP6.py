#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola mundo")

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
def calcular_area_circulo(radio):
    print(3,1416 * radio**2)

def calcular_perimetro_circulo(radio):
    print(2 * 3.1416 * radio)

#Ejercicio 5
def segundos_a_horas(segundos):
    print(segundos / 60)

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(i * numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir entre cero"

    print(f"suma = {suma}, resta = {resta}, multiplicacion = {multiplicacion}, division = {division}")

#Ejercicio 8
def calcular_imc(peso, altura):
    print(peso / altura **2)

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    print(celsius * 9/5 + 32)

#Ejercicio 10
def calcular_promedio(a, b, c):
    print((a + b + c) / 3)
