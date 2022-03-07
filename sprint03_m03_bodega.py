import random
import os
import time

# Funciones.

# Modificar stock de productos.
def modstock(modificar):
    if len(productos) == 0:
        print("No tenemos productos registrados.\n")
    else:
        print(f"\nUsted modificará el stock del producto {productos[modificar]}.\nSu stock actual es de {stock[modificar]} unidades.") # hasta aqui OK
        print("\nIngrese el número de unidades a modificar seguido de + o - (agregar o quitar)")
        mod = input("...\t")
        mod1 = mod[-1]
        if mod1 == "+":
            print(f"\nUsted agregará {mod[:-1]} unidades de {productos[modificar]}")
            stock[modificar] += int(mod[:-1])
            print(f"\nEl nuevo stock de {productos[modificar]} es de {stock[modificar]} unidades.")
        else:
            print(f"\nUsted quitará {mod[:-1]} unidades de {productos[modificar]}")
            if int(mod[:-1]) <= stock[modificar]:
                stock[modificar] -= int(mod[:-1])
                print(f"\nEl nuevo stock de {productos[modificar]} es de {stock[modificar]} unidades.")
            else:
                print("La operación no puede llevarse a cabo. Las unidades a quitar superan nuestro stock.\n")
    input("\nPresione ENTER para continuar... ")

# Agregar producto.
def agregarproducto():
    producto_agregar = input("Ingrese el nombre del producto: ")
    producto_stock = int(input("Ingrese el stock inicial del nuevo producto: "))
    producto_descrip = input("Ingrese infomación del producto: ")
    productos.append(producto_agregar)
    stock.append(producto_stock)
    descrip.append(producto_descrip)

# Eliminar producto.
def eliminarproducto():
    if len(productos) == 0:
        print("No tenemos productos registrados.")
    else:
        print("Eliminar Producto\n")
        for i in range(len(productos)):
            print('{:3}{:>15}'.format(i + 1, productos[i]))
        borrar = int(input("\nIngrese la opción del producto que desea eliminar: "))
        index_producto = borrar - 1    
        productos.pop(index_producto)
        stock.pop(index_producto)
        descrip.pop(index_producto)
        print("\nProducto Eliminado Correctamente!!")
    input("\nPresione ENTER para continuar... ")

# Ver stock de productos.
def verstock():
    alerta ="ALERTA: Quedan menos de 400 unidades"
    if len(productos) == 0:
        print("No tenemos productos.")
    else:
        print("Stock de todos los productos\n")
        print ('{:16} {:20} {:20}'.format("Producto", "Unidades", "Descripción", ""))
        print("*"*60)
        for i in range(len(productos)):
            time.sleep(1)
            if stock[i] < 400:
                print('{:16} {:<20} {:40} {:40}'.format(productos[i], stock[i], descrip[i], alerta))
            else:
                print('{:16} {:<20} {:20}'.format(productos[i], stock[i], descrip[i], ""))
    input("\nPresione ENTER para continuar...")

# variables para manejo de bodega
productos = ["Vasos", "Cucharas", "Cuchillos", "Tenedores"]
stock = [random.randint(300,500), random.randint(300,500), random.randint(300,500), random.randint(300,500)]
descrip = ["Cristal", "Acero Inoxidable", "Carnicero", "Suizos"]  

while True:
    os.system("cls")
    print("+++++ Te Lo Vendo +++++")
    print("+++++ Menú Principal +++++\n")
    print("[1] Manejo de Bodega.")
    print("[2] Información de Clientes.")
    print("[3] Sistema de Envío.")
    print("[4] Salir.")
    opcion = int(input("\nElija una opción:\t"))

    # Manejo de Bodega
    if opcion == 1:
        while True:
            os.system("cls")
            print("+++++ Te Lo Vendo +++++")
            print("+++++ Manejo de Bodega +++++\n")
            print("[1] Manipulación de stock de productos.")
            print("[2] Agregar producto.")
            print("[3] Eliminar producto.")
            print("[4] Ver stock de productos.")
            print("[5] Volver al Menú Principal.")
            opcion1 = int(input("\nElija una opción:\t"))

            if opcion1 == 1:        #Agregar o Quitar unidades de un producto.
                os.system("cls")
                print("+++++ Te Lo Vendo +++++")
                print("Modificación de Stock\n")
                if len(productos) == 0:
                    print("No tenemos productos registrados.\n")
                else:
                    for i in range(len(productos)):
                        print(f"[{i + 1}]\t{productos[i]}")
                    op11 = int(input("\nElija el producto a modificar:\t"))
                    modificar = op11 - 1
                    modstock(modificar)
                input("\nPresione ENTER para continuar... ")
            elif opcion1 == 2:      # Agregar producto.
                os.system("cls")
                agregarproducto()

            elif opcion1 == 3:      # Eliminar producto.     
                os.system("cls")
                eliminarproducto()

            elif opcion1 == 4:      # ver stock.
                os.system("cls")
                verstock()
                    
            elif opcion1 == 5:  #Volver al menu principal.
                break
            
    # Información de Clientes.
    elif opcion == 2:
        os.system("cls")
        print("Este módulo se desarrolló en el archivo sprint03_02_clientes.py")
        input("\nPresiones ENTER para continuar... ")

    # Sistema de Envío  .         
    elif opcion == 3:
        os.system("cls")
        print("Este módulo se desarrolló en el archivo sprint03_03_envios.py")
        input("\nPresiones ENTER para continuar... ")

    elif opcion == 4:
        break

os.system("cls")
print("Que tenga excelente jornada!.\n")
