#Ejercicio 1
notas = [10, 8, 8, 7, 9, 8, 10, 9, 6, 5]
sumatoria = 0
notaMasAlta = 0
notaMasBaja = 10
for nota in notas:
    sumatoria += nota
    if nota > notaMasAlta:
        notaMasAlta = nota
    if nota < notaMasBaja:
        notaMasBaja = nota
promedio = sumatoria / len(notas)

print(f"La nota mas alta es {notaMasAlta}, la nota mas baja es {notaMasBaja} y el promedio de las notas es {promedio}")

#Ejercicio 2
lista = []
while len(lista) != 5:
    lista.append(input("Por favor ingrese un producto: "))

print(sorted(lista))
lista.remove(input("Que elemento desea eliminar?: "))
print(sorted(lista))

#Ejercicio 3
import random
numeros = [random.randint(1, 100) for _ in range(15)]
print(numeros)
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

#Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos2 = set(datos)
print(datos2)

#Ejercicio 5
presentes = ["Matias", "Ezequiel", "Juan", "Nacho", "Damian", "Federico", "Maximo", "Santino"]
print(presentes)
accion = int(input("Ingrese 1 si desea agregar un nuevo estudiante\nIngrese 2 si desea eliminar un estudiante\n"))
if accion == 1:
    agregar = input("Ingrese el nombre del estudiante que desea agregar: ")
    presentes.append(agregar)
elif accion == 2:
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    presentes.remove(eliminar)
print(presentes)

#Ejercicio 6
numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)
numeros = [numeros[-1]] + numeros[:-1]
print("Lista rotada:", numeros)

#Ejercicio 7
temperaturas = [
    [10, 22],
    [12, 25],
    [9, 21],
    [11, 24],
    [8, 20],
    [13, 26],
    [10, 23]
]
prom_min = sum(t[0] for t in temperaturas) / len(temperaturas)
prom_max = sum(t[1] for t in temperaturas) / len(temperaturas)
print(f"Promedio mínimas: {prom_min:.2f}")
print(f"Promedio máximas: {prom_max:.2f}")
amplitudes = [t[1] - t[0] for t in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print(f"Mayor amplitud térmica el día {dia_mayor_amplitud} ({max(amplitudes)}°)")

#Ejercicio 8
notas = [
    [8, 6, 7],
    [5, 9, 8],
    [6, 5, 7],
    [9, 8, 10],
    [7, 7, 6]
]
print("Promedio por estudiante:")
for i, fila in enumerate(notas, start=1):
    prom = sum(fila) / len(fila)
    print(f"Estudiante {i}: {prom:.2f}")

print("\nPromedio por materia:")
for j in range(len(notas[0])):
    prom = sum(notas[i][j] for i in range(len(notas))) / len(notas)
    print(f"Materia {j+1}: {prom:.2f}")

#Ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
for fila in tablero:
    print(" ".join(fila))
print()
fila = int(input("Jugador X - Ingrese fila (0-2): "))
col = int(input("Jugador X - Ingrese columna (0-2): "))
tablero[fila][col] = "X"
for fila in tablero:
    print(" ".join(fila))
print()
fila = int(input("Jugador O - Ingrese fila (0-2): "))
col = int(input("Jugador O - Ingrese columna (0-2): "))
tablero[fila][col] = "O"
for fila in tablero:
    print(" ".join(fila))
print()

#Ejercicio 10
ventas = [
    [10, 15, 12, 8, 20, 25, 18],
    [5, 7, 9, 6, 10, 12, 8],
    [12, 14, 10, 9, 15, 20, 17],
    [8, 6, 7, 10, 12, 15, 9]
]
print("Total vendido por producto:")
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    print(f"Producto {i}: {total}")

totales_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = totales_dia.index(max(totales_dia)) + 1
print(f"\nDía con mayores ventas: Día {dia_max} (Total: {max(totales_dia)})")
totales_producto = [sum(fila) for fila in ventas]
producto_top = totales_producto.index(max(totales_producto)) + 1
print(f"Producto más vendido: Producto {producto_top} (Total: {max(totales_producto)})")
