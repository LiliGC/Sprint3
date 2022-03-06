#Creacion de listas con los datos de los clientes:
#nombre, apellido, edad, contraseña,idclientes. Y es correlativo de acuerdo al índice de la lista.
#También incluyo la ubicación para relacionarlo con el sistema de envío. Siendo A menor a 1000Km y B mayor a 1000Km.
nombre=["Abel","Susana","Pedro","Ana"]
apellido = ["Dormido", "Oria", "Pérez", "Fernández"]
edad=[40,25,32,36]
contrasena=["Ab@25","Sn@35","Pb@60","An@16"]
idclientes = [2022001, 2022002, 2022003, 2022004]
ubicación=["A","B","A","B"]
#Creación de función para mostrar de todos los clientes registrados.en forma de tabla.
def mostrar_clientes():
    print("Los clientes registrados son los siguientes:\n")
    print ('{:15}{:15}''{:5}{:18}{:12}{:12}'.format("Nombre","Apellido","Edad","Id","Contraseña","Ubicación"))
    print("*"*75)
    for i in range(len(nombre)):
        print('{:<15}{:15}''{:<5}{:<18}{:<12}{:<12}'.format(nombre[i], apellido[i],edad[i],idclientes[i],contrasena[i],ubicación[i]))
#Creación de función para agregar al cliente, nombre, edad, contraseña, y el id se coloca en forma automática de acuerdo al último de la lista.
def agregarcliente():
    nombre_agregar = input("Ingrese el nombre del cliente: ").title()
    apellido_agregar=input("Ingrese el apellido del cliente:").title()
    edad_agregar=int(input("Ingrese la edad del cliente:"))
    cliente_id = idclientes[-1]+1
    ubicacion_agregar=input("Ingrese su ubicación(A o B), siendo A <1000Km y B>1000Km: ").upper()
    contrasena_agregar=(input("Ingrese su contraseña(Recuerde que debe tener 1 mayúscula,número y símbolo):"))
    nombre.append(nombre_agregar)
    apellido.append(apellido_agregar)
    edad.append(edad_agregar)
    idclientes.append(cliente_id)
    contrasena.append(contrasena_agregar)
    ubicación.append(ubicacion_agregar)
    print("El cliente se ha agregado exitosamente.")
#Creación de función para remover cliente pregunta el nombre a eliminar, pregunta cuál se desea eliminar. y así se sabe el índice en la lista.
#Teniendo este dato eliminamos el id correspondiente.
def removercliente():
    id_eliminar=int(input("Ingrese el id del cliente a eliminar:"))
    if id_eliminar in idclientes:
        indice_eliminar=idclientes.index(id_eliminar)
        idclientes.pop(indice_eliminar)
        nombre.pop(indice_eliminar)
        apellido.pop(indice_eliminar)
        contrasena.pop(indice_eliminar)
        ubicación.pop(indice_eliminar)
        print("El cliente se ha eliminado con éxito")
    else: print("El cliente no se encuentra registrado en nuestra aplicación")
#Creación de función para consultar por un cliente en específico. Me muestra una tabla con sus datos.
def mostrar_particular():
    cliente_particular=input("Ingrese el nombre del cliente que desea ver sus datos:").title()
    a=nombre.index(cliente_particular)
    print("Los datos del cliente son los siguientes\n")
    print ('{:15}{:15}''{:5}{:15}{:12}{:12}'.format("Nombre", "Apellido", "Edad", "Id", "Contraseña","Ubicación"))
    print("*"*75)
    if cliente_particular in nombre:
        print('{:<15}{:15}''{:<5}{:<15}{:<12}{:<12}'.format(nombre[a], apellido[a], edad[a], idclientes[a], contrasena[a],ubicación[a]))
    else: print("El cliente no se encuentra registrado en nuestra aplicación")

#Menu de la Base de datos clientes
while True:
            print("\n-----Base de datos de Clientes: Te lo vendo Market-----\n")
            print("[1] Ver Clientes registrados.")
            print("[2] Agregar Clientes")

            print("[3] Eliminar Clientes.")
            print("[4] Ver datos de un cliente en particular.")
            print("[5] Volver al Menú Principal.\n")

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
#4. Mostrar a un cliente en particular.
            elif opcion2 == 4:
                mostrar_particular()
            elif opcion2 == 5:
                break
