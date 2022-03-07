import random
import os
import time

# Funciones

# Estado Bodegas de Envío.
def bodegasenvio():
    stock_A = 0         # Inicialmente las bodegas de envío se encuentran vacías
    stock_B = 0         # ya que no se ha simulado alguna compra.
                
    # Conteo de productos en cada bodega de envío.
    for i in range(len(bodega_A)):          # suma de unidades de bodega A
        stock_A += bodega_A[i]

    for i in range(len(bodega_B)):          # suma de unidades de bodega B
        stock_B += bodega_B[i]
                    
    suma = stock_A + stock_B 

    # % de capacidad de almacenaje de cada bodega.
    cap_A = stock_A*100/500
    cap_B = stock_B*100/500
                
    # Mensajes de alertas inicialmente vacías.
    alerta_A = ""
    alerta_B = ""

    if suma == 0:           # Si la suma de unidades en ambas bodegas es 0, no hay nada por despachar.
        os.system("cls")
        print("Nuestras Bodegas no tienen productos para ser despachados.")
        input("Presione ENTER para continuar... ")

    else:                   # En otro caso..
        os.system("cls")
        if cap_A >= 100:    # Bodega A llena.
            alerta_A = "ADVERTENCIA: Se ha llenado la bodega"
                    
        if cap_B >= 100:    # Bodega B llena.    
            alerta_B = "ADVERTENCIA: Se ha llenado la bodega"

        print(f"Bodega A: {stock_A} unidades.\t{cap_A}% de bodega utilizada\t{alerta_A}")
        print(f"Bodega B: {stock_B} unidades.\t{cap_B}% de bodega utilizada\t{alerta_B}")
        input("\nPresione ENTER para continuar... ")

# Simular compra y envío.
def compraenvio():
    os.system("cls")

    compra_usuario = random.randint(0, len(nombres) - 1) # indice de usuario que compra
    compra_producto = random.randint(0, len(productos) - 1) # indice de producto que compra el usuario
    compra_id = ids[compra_usuario] # id del usuario que compra
    compra_n = random.randint(25,100) # n unidades de producto que compra el usuario, te utiliza este rango para hacer mas rápida la simulación.
        
    compra_envio = ubicaciones[compra_usuario] # ubicacion del usuario que compra
        
    compra_stock = stock[compra_producto] #stock de unidades del producto que se compra

    print(f"Bienvenid@ {nombres[compra_usuario]} nº id: {compra_id}")
    print(f"Has seleccionado comprar {compra_n} unidades de {productos[compra_producto]}")
    print(f"Tu domicilio se ubica a {compra_envio} km de nuestra bodega matriz.")

    if stock[compra_producto] >= 1 and stock[compra_producto] >= compra_n:
        stock[compra_producto] -= compra_n

        if compra_envio > 1000:
            print("El tipo de envío es: LARGO, tus productos se despacharán a nuestra bodega B")
            bodega_B.append(compra_n)
        else:
            print("El tipo de envío es: RÁPIDO, tus productos se despacharán a nuestra bodega A")
            bodega_A.append(compra_n)
            print("Compra realizada exitosamente!")
            print(f"\nQuedan {stock[compra_producto]} unidades de {productos[compra_producto]}")
                    
    else:
        print("Producto Agotado!")

    input("Presione ENTER para continuar... ")


# variables para manejo de bodega
productos = ["Vasos", "Cucharas", "Cuchillos", "Tenedores"]
stock = [random.randint(300,500), random.randint(800,1900), random.randint(300,500), random.randint(900,1500)]
descrip = ["Cristal", "Acero Inoxidable", "Carnicero", "Suizos"]    # Para este módulo no es de importancia.

# variables para informacion clientes
ids = [2022001, 2022002, 2022003, 2022004]
nombres =  ["Susana Oria", "Alejandro Magnolon", "Mateo Toro", "Michelle Michellini"]
nombre = ["Susana", "Alejandro", "Mateo", "Michelle"]
apellido = ["Oria", "Magnolon", "Toro", "Michellini"]
edades =  [32, 48, 53, 68]
contrasenas = ["susanitaBeLla", "cieloAZULADO78", "vivaelPULENTO666", "Y0n0FU1*"]
# Se crea la lista "ubicaciones" para almacenar la distancia del domicilio del cliente a la bodega central.
# Se utiliza ese rango para el valor aleatorio para que puedan trabajarse en la muestra con ubicacion > 1000 km.
ubicaciones = [random.randint(900,1200), random.randint(832,1200), random.randint(900,1200), random.randint(900,1200)]

# variables para sistema de envio
bodega_A = [0]*len(productos) #bodega envio rapido < 1000 km
bodega_B = [0]*len(productos) #bodega envio largo > 1000 km

while True:
    os.system("cls")
    print("+++++ Te Lo Vendo +++++\n")
    print("+++++ Menú Principal +++++\n")
    print("[1] Manejo de Bodega.")
    print("[2] Información de Clientes.")
    print("[3] Sistema de Envío.")
    print("[4] Salir.")
    opcion = int(input("\nElija una opción:\t"))

    # Manejo de Bodega
    if opcion == 1:
        print("Desarrollamos este módulo en el archivo sprint03_bodega.py")
        input("\nPresiones ENTER para continuar... ")
 
    # Información de Clientes
    elif opcion == 2:
        print("Desarrollamos este módulo en el archivo sprint03_clientes.py")
        input("\nPresiones ENTER para continuar... ")

    # Sistema de Envío           
    elif opcion == 3:
        os.system("cls")
        print("+++++ Te Lo Vendo +++++\n")
        print("+++++ Sistema de Envío +++++\n")
        print("[1] Ver Stock de Bodegas.")
        print("[2] Simular compra y sistema de envío.")
        print("[3] Salir.")
        opcion = int(input("\nElija una opción:\t"))

        while True:
            if opcion == 1:         # Stock de bodegas de envío.
                bodegasenvio()
                break
            elif opcion == 2:           # Simular compra y sistema de envío.
                compraenvio()
                break

            elif opcion == 3:
                break
    
    elif opcion == 4: 
        break

os.system("cls")
print("Que tenga excelente jornada!.\n")
    
