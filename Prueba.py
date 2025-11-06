#Ejercicio 5
presentes = ["Matias", "Ezequiel", "Juan", "Nacho", "Damian", "Federico", "Maximo", "Santino"]
print(presentes)
accion = int(input("Ingrese 1 si desea agregar un nuevo estudiante\nIngrese 2 si desea eliminar un estudiante"))
if accion == 1:
    agregar = input("Ingrese el nombre del estudiante que desea agregar")
    presentes.append(agregar)
elif accion == 2:
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar")
    presentes.remove(eliminar)
print(presentes)