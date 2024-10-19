# GestionInventario
Scrip con sistema de gestión de inventario para tiendas en línea, que permite manejar productos genéricos y electrónicos, realizar ventas, y controlar el stock de forma eficiente. Se basa en la Programación Orientada a Objetos (POO), con clases ,herencia y manejo de excepciones.

Estructura del Proyecto
Clases
  1.Producto:
    *Representa un producto genérico.
    *Atributos:
       _nombre (string): Nombre del producto.
       _precio (float): Precio del producto.
       _stock (int): Cantidad disponible en inventario.
    *Métodos:
       __init__(self, nombre, precio, stock): Constructor de la clase.
       get_nombre(self): Devuelve el nombre del producto.
       get_precio(self): Devuelve el precio del producto.
       set_precio(self, nuevo_precio): Establece un nuevo precio para el producto, validando que no sea negativo.
       introducir_stock(self, cantidad): Aumenta el stock del producto.
       retirar_stock(self, cantidad): Reduce el stock del producto.
  2.ProductoElectronico (hereda de Producto):
    *Representa un producto electrónico, que además de los atributos del producto genérico incluye una garantía.
    *Atributos:
        _garantia (int): Duración de la garantía en meses.
    *Métodos:
       __init__(self, nombre, precio, stock, garantia): Constructor de la clase.
       get_garantia(self): Devuelve el periodo de garantía.
       set_garantia(self, nueva_garantia): Establece un nuevo periodo de garantía, asegurando que sea positivo.
       
Excepciones
 *ValueError: Captura valores no válidos como precios o stock negativos.
 *Entradas
    -El programa toma entradas para agregar productos al inventario. Estas entradas incluyen:
    -Nombre del producto.
    -Precio del producto.
    -Stock disponible.
    -(Para productos electrónicos) Periodo de garantía.
 *Salidas
    -El programa ofrece las siguientes salidas:
    -Visualización del estado actual del inventario.
    -Información detallada sobre cada producto y su stock.
    -Notificación en caso de que no haya suficiente stock para realizar una venta.

Métodos Principales
 *mostrar_info(): Muestra los datos de un producto o producto electrónico.
 *introducir_stock(cantidad): Permite agregar unidades de un producto al inventario.
 *retirar_stock(cantidad): Permite retirar unidades de un producto del inventario si están disponibles.
 *realizar_venta(nombre_producto, cantidad): Gestiona la venta de un producto, actualizando el inventario en tiempo real.

 USO
 #Crear un producto genérico
producto1 = Producto("Camisa", 25.99, 100)

#Crear un producto electrónico
producto_elec = ProductoElectronico("Laptop", 999.99, 50, 24)

#Mostrar información de los productos
producto1.mostrar_info()
producto_elec.mostrar_info()

#Introducir más stock
producto1.introducir_stock(50)

#Realizar una venta
producto1.retirar_stock(10)
