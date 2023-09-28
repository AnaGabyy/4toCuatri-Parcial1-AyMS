import datetime

class Producto:
    def __init__(self):
        self.id_producto = None
        self.nombre = None
        self.marca = None
        self.descripcion = None
        self.precio = None
        self.stock = None
        self.fecha_vencimiento = None
        self.restringido = None
        self.id_categoria = None
        self.id_proveedor = None

    def agregar_nombre(self, nombre):
        self.nombre = nombre

    def agregar_marca(self, marca):
        self.marca = marca

    def agregar_descripcion(self, descripcion):
        self.descripcion = descripcion

    def agregar_precio(self, precio):
        self.precio = precio

    def agregar_stock(self, stock):
        self.stock = stock

    def agregar_fecha_vencimiento(self, año, mes, dia):
        self.fecha_vencimiento = datetime.datetime(año, mes, dia)

    def agregar_restringido(self, restringido):
        if isinstance(restringido, bool):  # Para verificar que sea un booleano
            self.restringido = restringido
        else:
            raise ValueError("El valor de 'restringido' debe ser un booleano")

    def agregar_id_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def agregar_id_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor

    def mostrar(self):
        return f"Producto: {self.nombre}, Marca: {self.marca}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}, Fecha de vencimiento: {self.fecha_vencimiento}, Restringido: {self.restringido}, ID de la categoria: {self.id_categoria}, ID del proveedor: {self.id_proveedor}"

# Ejemplo
producto = Producto()
producto.agregar_nombre("Limpiador Multiusos")
producto.agregar_marca("Cif")
producto.agregar_descripcion("Acá va la descripción del producto.")
producto.agregar_precio(569.99)
producto.agregar_stock(190)
producto.agregar_fecha_vencimiento(2025, 10, 23)
producto.agregar_restringido(False)
producto.agregar_id_categoria(1)
producto.agregar_id_proveedor(2)

print(producto.mostrar())
