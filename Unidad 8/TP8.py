import os

NOMBRE_ARCHIVO = "productos.txt"

#funciones extra

def leer_productos():
    """Lee el archivo y retorna una lista de diccionarios con los productos."""
    productos = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo de productos no existe. Se devolverá una lista vacía.")
        return productos

    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                try:
                    nombre, precio, cantidad = partes
                    producto = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    }
                    productos.append(producto)
                except ValueError:
                    print(f"Error al procesar la línea: {linea.strip()}. Saltando.")
    return productos

def guardar_productos(productos):
    """Sobrescribe el archivo con los productos actualizados de la lista."""
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        lineas = []
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            lineas.append(linea)
        
        archivo.writelines(lineas)
    print("\nDatos guardados y archivo actualizado correctamente.")


def mostrar_productos(productos):
    """Muestra los productos en el formato solicitado."""
    if not productos:
        print("\n--- No hay productos para mostrar. ---")
        return
        
    print("\n--- LISTADO DE PRODUCTOS ---")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")
    print("----------------------------")

#Ejercicio 1
def actividad_1_crear_inicial():
    """Crea el archivo inicial si no existe."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Creando archivo inicial: {NOMBRE_ARCHIVO}")
        datos_iniciales = [
            "Lapicera,120.5,30\n",
            "Cuaderno A4,550.0,15\n",
            "Mochila,4500.99,5\n"
        ]
        with open(NOMBRE_ARCHIVO, "w") as archivo:
            archivo.writelines(datos_iniciales)
        print("Archivo inicial creado con éxito.")
    else:
        print(f"El archivo {NOMBRE_ARCHIVO} ya existe. Saltando creación inicial.")

#Ejercicio 3
def actividad_3_agregar_producto():
    """Pide datos al usuario y los añade al archivo sin borrar el contenido."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Ingrese el nombre del nuevo producto: ")
    
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Precio inválido. Ingrese un número.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Cantidad inválida. Ingrese un número entero.")

    nueva_linea = f"{nombre},{precio},{cantidad}\n"

    with open(NOMBRE_ARCHIVO, "a") as archivo:
        archivo.write(nueva_linea)
        
    print(f"\n Producto '{nombre}' agregado al archivo.")
    
#Ejercicio 5
def actividad_5_buscar_producto(productos):
    """Busca un producto en la lista cargada en memoria."""
    print("\n--- BUSCAR PRODUCTO ---")
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False

    for p in productos:
        if p['nombre'].lower() == nombre_buscado.lower():
            print(f"\n Producto Encontrado:")
            print(f"  Nombre: {p['nombre']}")
            print(f"  Precio: ${p['precio']:.2f}")
            print(f"  Cantidad: {p['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nERROR: El producto '{nombre_buscado}' no existe.")

def main():
    # 1
    actividad_1_crear_inicial() 

    # 4
    productos_en_memoria = leer_productos()

    # 2
    mostrar_productos(productos_en_memoria)

    # 3
    actividad_3_agregar_producto()
    productos_en_memoria = leer_productos()
    
    # 5
    actividad_5_buscar_producto(productos_en_memoria)
    
    # 6
    guardar_productos(productos_en_memoria)
