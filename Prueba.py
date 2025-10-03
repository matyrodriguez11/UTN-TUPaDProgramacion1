#Ejercicio 10
numero = int(input("Ingresa un número: "))
numeroInvertido = 0

while numero > 0:
    digito = numero % 10
    numeroInvertido = numeroInvertido * 10 + digito
    numero //= 10

print(numeroInvertido)