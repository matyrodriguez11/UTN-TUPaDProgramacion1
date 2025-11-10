#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1) Diccionario actualizado con nuevas frutas:")
print(precios_frutas)
print()

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2) Diccionario con precios actualizados:")
print(precios_frutas)
print()

#Ejercicio 3
frutas = list(precios_frutas.keys())
print("3) Lista de frutas sin precios:")
print(frutas)
print()

#Ejercicio 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese un nombre para consultar su número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")
print()

#Ejercicio 5
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
unicas = set(palabras)
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Palabras únicas:", unicas)
print("Cantidad de apariciones:", conteo)
print()

#Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")
print()

#Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Aprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)
print()

#Ejercicio 8
stock = {"Harina": 10, "Aceite": 5, "Azúcar": 8}
producto = input("Ingrese el producto a consultar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Desea agregar unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese cantidad a agregar: "))
        stock[producto] += cantidad
else:
    print("Producto no existente. Se agregará al stock.")
    cantidad = int(input("Ingrese cantidad inicial: "))
    stock[producto] = cantidad

print("Stock actualizado:", stock)
print()

#Ejercicio 9
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de Python",
    ("Viernes", "18:00"): "Entrega del TP"
}
dia = input("Ingrese un día: ")
hora = input("Ingrese una hora (hh:mm): ")

evento = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print(f"Evento: {evento}")
print()

#Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido (capitales como claves):")
print(capitales_paises)