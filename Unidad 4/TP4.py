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
inicial = int(input("Por favor ingresa un numero entero inicial"))
final = int(input("Por favor ingresa un numero entero final"))
sumatoria = 0
for i in range ((inicial+1), (final)):
    sumatoria += i
print(sumatoria)

