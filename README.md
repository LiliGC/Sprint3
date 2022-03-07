# Bootcamp Full Stack Python: Módulo 3 “Te lo vendo” - Sprint

Grupo 1: Alberto Briones, Liliana Garmendia, Diego González

GitHub: https://github.com/LiliGC/Sprint3

“La empresa “Te lo Vendo” es un emprendimiento de un grupo de jóvenes, quienes necesitan vender sus productos en línea. Actualmente toman sus pedidos vía telefónica y a través del correo electrónico. Al no existir un sistema centralizado para los pedidos, es complejo tener control oportuno de las entregas, lo que genera que en algunos casos no se concreten algunos pedidos.	
Una opción propuesta es manejar una planilla de cálculo para el registro de los pedidos y realización de seguimiento. Si bien es factible su uso, a medida que se agreguen nuevos clientes el archivo irá creciendo, y será complejo mantener la integridad entre los datos, impidiendo relacionarlos adecuadamente”. 
La solución entregada es un programa que posee tres módulos: manejo de bodega, información de clientes y sistema de envío. Cada módulo fue desarrollado en un archivo distinto. A continuación, se realizan algunas observaciones respecto al desarrollo de los códigos de cada módulo. 

Manejo de bodega:
En el código del archivo sprint03_m03_bodega.py se incorporó un menú que permite acceder a las operaciones solicitadas para este sprint. Creamos funciones para agregar productos a la bodega virtual, modificar el stock de unidades de un producto en particular, eliminar producto, mostrar stock de unidades de productos (todos, disponibles para venta, cuyo stock es superior a n unidades).

Información de clientes:
En el archivo sprint03_m03_clientes.py trabajamos con un diccionario con listas de la información de clientes, creamos funciones para agregar clientes: nombre, apellido, edad, número de identificación de clientes (ID), contraseña y ubicación (del domicilio del cliente respecto a la bodega central). Decidimos agregar este último punto, ya que es útil para el desarrollo del módulo de Sistema de Envío. También se cuenta con opción de eliminar clientes según su ID, mostrar los clientes registrados en forma de una tabla (importando el módulo tabulate). Y presentamos estos a través de un menú en la consola con el que se accede a las opciones de la Base de datos de clientes.

Sistema de envío:
En el archivo sprint03_m03_envios.py implementamos un sistema de visualización de bodegas de envíos. Para poder manejar estas bodegas, era necesario simular compras, así, existiría un flujo de unidades de productos desde la bodega central hacia las de envío. En el menú de este módulo, se tiene acceso al estado de las bodegas, en donde, en caso de alcanzar o superar el porcentaje de almacenaje (consideramos 400 unidades en general, de todos los productos) se avisa por pantalla sobre esto y se ve un mensaje de alerta. Además, se tiene acceso en el menú a simular una compra y un envío. Este sistema consiste en la compra de m unidades de un producto, ambos aleatorios, y de un cliente registrado escogido aleatoriamente. El sistema de envío determinará a que bodega se enviarán las unidades del producto. Tras realizar la compra, el resultado de disminución de stock se ve reflejado en el visor de estado de las bodegas de envío, mostrándose la capacidad utilizada.
 



