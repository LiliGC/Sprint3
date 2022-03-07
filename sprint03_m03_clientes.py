from tabulate import tabulate
#Creacion de un diccionario de los clientes con listas con  las siguientes características.
#nombre, apellido, edad, contraseña,idclientes que se agrega automático respecto al índice del último de la lista. También se agrega la ubicación siendo A  menor a 1000Km de distancia
#de  la tienda central de Telovendo Market y B si está a mas de 1000Km de distancia. Esto para relacionarlo al sistema de envío .

Clientes={"Nombre":["Abel","Susana","Pedro","Ana"],
        "Apellido": ["Dormido", "Oria", "Pérez", "Fernández"],
        "Edad":[40,25,32,36],
        "Contraseña":["Ab@25","Sn@35","Pb@60","An@16"],
        "Idclientes":[2022001, 2022002, 2022003, 2022004],
        "Ubicacion":["A","B","A","B"]}

#Creación de función para mostrar de todos los clientes registrados.en forma de tabla al importar el módulo tabulate.

def mostrar_clientes():
    print(tabulate(Clientes, headers="keys", tablefmt="fancy_grid"))
#Creación de función para agregar al cliente, nombre, edad, contraseña,el id se coloca en forma automática de acuerdo al último de la lista y la ubicación.

def agregarcliente():
    nombre_agregar = input("Ingrese el nombre del cliente: ").title()
    apellido_agregar=input("Ingrese el apellido del cliente:").title()
    edad_agregar=int(input("Ingrese la edad del cliente:"))
    cliente_id = Clientes["Idclientes"][-1]+1
    contrasena_agregar=(input("Ingrese su contraseña(Recuerde que debe tener 1 mayúscula,número y símbolo):"))
    ubicacion_agregar=input("Ingrese su ubicación(A o B), siendo A <1000Km y B>1000Km: ").upper()
    Clientes["Nombre"].append(nombre_agregar)
    Clientes["Apellido"].append(apellido_agregar)
    Clientes["Edad"].append(edad_agregar)
    Clientes["Idclientes"].append(cliente_id)
    Clientes["Contraseña"].append(contrasena_agregar)
    Clientes["Ubicacion"].append(ubicacion_agregar)
    print("\nEl cliente se ha agregado exitosamente.")
#Creación de función para remover cliente pregunta el Id a eliminar, con esto sabemos el indice que ocupa en la lista de IdClientes
#Teniendo este dato eliminamos el id correspondiente usando el método pop.

def removercliente():
    id_eliminar=int(input("Ingrese el Id del cliente a eliminar:"))
    if id_eliminar in Clientes["Idclientes"]:
        indice_eliminar=Clientes["Idclientes"].index(id_eliminar)
        Clientes["Idclientes"].pop(indice_eliminar)
        Clientes["Nombre"].pop(indice_eliminar)
        Clientes["Edad"].pop(indice_eliminar)
        Clientes["Apellido"].pop(indice_eliminar)
        Clientes["Contraseña"].pop(indice_eliminar)
        Clientes["Ubicacion"].pop(indice_eliminar)
        print("El cliente se ha eliminado con éxito")
    else: print("El cliente no se encuentra registrado en nuestra aplicación")

#Menu de la Base de datos clientes
while True:
            print("\n-----Base de datos de Clientes: Te lo vendo Market-----\n")
            print("[1] Ver Clientes registrados.")
            print("[2] Agregar Clientes")
            print("[3] Eliminar Clientes.")
            print("[4] Salir.\n")

            opcion2 = int(input("Seleccione una opción: "))
# 1. Mostrar clientes registrados.
            if opcion2 == 1:
                mostrar_clientes()
# 2. Agregar clientes
            elif opcion2 == 2:
                agregarcliente()
# 3. Remover clientes
            elif opcion2 == 3:
                removercliente()
#4. Salir de la base de datos de Clientes.
            elif opcion2 == 4:
                break
