# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    # Getters y setters para controlar los atributos privados
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = value

    def mostrar_info_producto(self):
        return f"Producto: {self._nombre}, Precio: ${self._precio}, Stock: {self._stock} unidades."

    def vender(self, cantidad):
        if cantidad > self._stock:
            raise Exception(f"No hay suficiente stock para {self._nombre}. Stock disponible: {self._stock}.")
        self._stock -= cantidad
        print(f"Se han vendido {cantidad} unidades de {self._nombre}.")


# Clase heredada ProductoElectronico
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self._garantia = garantia  # En meses

    # Getter y setter para la garantía
    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, value):
        if value < 0:
            raise ValueError("La garantía no puede ser negativa.")
        self._garantia = value

    def mostrar_info_producto(self):
        return f"Producto Electrónico: {self._nombre}, Precio: ${self._precio}, Stock: {self._stock}, Garantía: {self._garantia} meses."


# Clase de gestión de inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto.mostrar_info_producto()}")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto.mostrar_info_producto())

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        raise Exception("Producto no encontrado.")

    def vender_producto(self, nombre, cantidad):
        try:
            producto = self.buscar_producto(nombre)
            producto.vender(cantidad)
        except Exception as e:
            print(f"Error: {e}")


# Uso del inventario
def main():
    try:
        # Inicializamos el inventario
        inventario = Inventario()

        # Crear algunos productos
        producto1 = Producto("Sudadera", 20, 50)
        producto2 = Producto("Pantalón", 40, 30)
        producto3 = Producto("Vestido", 30, 20)
        producto_electro1 = ProductoElectronico("Computadora", 1500, 10, 24)  # 24 meses de garantía
        producto_electro2 = ProductoElectronico("Cámara",1000 , 10, 12)  # 24 meses de garantía

        # Agregar productos al inventario
        inventario.agregar_producto(producto1)
        inventario.agregar_producto(producto2)
        inventario.agregar_producto(producto3)
        inventario.agregar_producto(producto_electro1)
        inventario.agregar_producto(producto_electro2)

        # Mostrar el inventario actual
        print("\nInventario actual:")
        inventario.mostrar_inventario()

        # Vender productos
        print("\nVenta de productos:")
        inventario.vender_producto("Pantalón", 5)
        inventario.vender_producto("Telefono", 2)
        inventario.vender_producto("Cámara", 2)

        # Mostrar el inventario después de las ventas
        print("\nInventario después de la venta:")
        inventario.mostrar_inventario()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")


if __name__ == "__main__":
    main()