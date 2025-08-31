#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
nombre = input("Por favor ingrese su nombre")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Por favor ingrese su nombre")
apellido = input("Por favor ingrese su apellido")
edad = input("Por favor ingrese su edad")
paisDeResidencia = input("Por favor ingrese su pais de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {paisDeResidencia}")

#Ejercicio 4
radio = int(input("Por favor ingrese el radio de un circulo"))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"el area  del circulo es {area} y el perimetro es {perimetro}")

#Ejercicio 5
segundos = int(input("Por favor ingrese una cantidad de segundos"))
horas = segundos / 60
print(f"{segundos} segundos son {horas} horas")

#Ejercicio 6
numero = int(input("Por favor ingrese un numero"))
print(numero)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)

#Ejercicio 7
numero1 = int(input("Por favor ingrese un numero entero que sea distinto de cero"))
numero2 = int(input("Por favor ingrese otro numero entero que sea distinto de cero"))
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")

#Ejercicio 8
altura = float(input("Por favor ingrese su altura en metros "))
peso = float(input("Por favor ingrese su peso en kg "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es {imc}")

#Ejercicio 9
temperatura = float(input("Por favor ingrese una temperatura en grados  Celsius"))
equivalente = (9/5) * temperatura + 32
print(f"{temperatura} Celsius son {equivalente} grados Fahrenheit")

#Ejercicio 10
numero1 = float(input("Por favor ingrese un numero "))
numero2 = float(input("Por favor ingrese otro numero "))
numero3 = float(input("Por favor ingrese otro numero "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los numeros ingresados es: {promedio}")