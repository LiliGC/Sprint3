# Sprint3: Bootcamp Full Stack Python

Sprint 3: Bootcamp Full Stack Python 

Grupo 1: Alberto Briones, Liliana Garmendia, Diego González 

La empresa “Te lo Vendo” es un emprendimiento de un grupo de jóvenes, quienes necesitan vender sus productos en línea. Actualmente toman sus pedidos vía telefónica y a través del correo electrónico.Al no existir un sistema centralizado para los pedidos, es complejo tener control oportuno de las entregas, lo que genera que en algunos casos no se concreten algunos pedidos.
Una opción propuesta es manejar una planilla de cálculo para el registro de los pedidos y realización de seguimiento. Si bien es factible su uso, a medida que se agreguen nuevos clientes el archivo irá creciendo, y será complejo mantener la integridad entre los datos, impidiendo relacionarlos adecuadamente.

Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los procesos de negocio descritos y que proponga una mejora en la gestión, el control, la seguridad, y disponibilidad de información para el negocio y sus clientes. El sistema debe permitir presentar productos, tomar pedidos y hacer seguimiento de estos y la gestión de clientes. Además, se requiere que el sistema genere reportes y estadísticas que ayuden a tomar de decisiones y mejorar el rendimiento de
la empresa, considerando la cantidad de clientes, y la demanda de éstos. Es imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.

La solución entregada es un programa que tiene tres partes: manejo de bodega, información clientes y sistema de envío.  

En el manejo de bodega creamos funciones para agregar productos a la bodega virtual, sumarle o restarle unidades a los productos, eliminar productos de la bodega virtual, mostrar todos los productos disponibles junto con su stock, y un mensaje de alerta cuando los productos tengan menos de 400 unidades. Y presentamos estos a través de un menú en la consola al que se accede al control de bodega. 

En la información de clientes creamos un diccionario con listas con la información de clientes, creamos funciones para agregar clientes(nombre, apellido, edad, Idclientes, contraseña y ubicación), eliminar clientes según su Id, y otra función para mostrar los clientes registrados en forma de una tabla importando el módulo tabulate, usando las keys del diccionario para las columnas. Y presentamos estos a través de un menú en la consola con el que se accede a las opciones de la Base de datos de clientes. 

Por último, en el sistema de envío creamos una función para comprar en forma aleatoria un producto, elección de un cliente al azar e indicar basándonos en la ubicación del Cliente si este va a recibir un envío rápido de la bodega A o un envío largo de la bodega B. Los productos se van almacenar en las listas de estas dos bodegas. Y el programa va a indicar cuando se llegue al máximo de 500 unidades por bodega. Esto también se presenta con un menú en consola donde da la opción de comprar, ver si su envío es rápido o largo, y el stock de productos en las bodegas. 



