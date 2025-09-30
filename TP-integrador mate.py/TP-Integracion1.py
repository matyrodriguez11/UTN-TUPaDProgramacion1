import time

#Declaramos la lista
numeros_Binarios = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

#Inicializamos el contador
contador = 0

#Comenzamos el programa
print("Contamos de 0 a 15 en binario:\n")

for numero in numeros_Binarios: #Recorremos toda la lista
    print(contador, "=", numero) 
    contador+= 1 #Incrementamos el contador
    time.sleep(1.25) #Retraso de un segundo

#Finalizamos el programa
print("\nFin del programa")     