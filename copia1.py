import time
from functools import wraps

# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, stock, categoria, tipo=None, fecha_vencimiento=None, garantia=None):
        self.codigo = codigo  # atributo público
        self._nombre = nombre  # atributo protegido
        self.__precio = precio  # atributo privado
        self.stock = stock
        self.categoria = categoria
        self.tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.garantia = garantia

    # Propiedad para el atributo protegido
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # Propiedad para el atributo privado
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor

# Función para cargar productos mediante unpacking desde una lista de datos
def cargar_productos(lista_datos):
    productos = [Producto(*datos) for datos in lista_datos]
    return productos

# Decoradores
def registrar_operacion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Iniciando operación: {func.__name__}")
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Operación completada en {fin - inicio:.2f} segundos")
        return resultado
    return wrapper

# Método para aplicar descuentos masivos usando map
@registrar_operacion
def aplicar_descuentos(productos, porcentaje_descuento):
    def aplicar_descuento(producto):
        producto.precio *= (1 - porcentaje_descuento / 100)
        return producto
    return list(map(aplicar_descuento, productos))

# Funciones para calcular totales con sum
@registrar_operacion
def calcular_valor_inventario(productos):
    return sum(producto.precio * producto.stock for producto in productos)

# Excepciones personalizadas
class ProductoError(Exception):
    pass

class StockInsuficienteError(ProductoError):
    def __init__(self, mensaje="Stock insuficiente para la operación"):
        super().__init__(mensaje)

# Método para generar reportes utilizando unpacking y map
@registrar_operacion
def generar_reporte(productos):
    return [f"Producto: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}" for producto in productos]

# Ejemplo de uso
lista_datos = [
    (1, "Producto A", 100, 50, "Categoría 1"),
    (2, "Producto B", 200, 20, "Categoría 2"),
    (3, "Producto C", 150, 30, "Categoría 3")
]

# Cargar productos
productos = cargar_productos(lista_datos)

# Aplicar descuentos
productos_con_descuento = aplicar_descuentos(productos, 10)

# Calcular valor de inventario
valor_total = calcular_valor_inventario(productos_con_descuento)
print(f"Valor total del inventario: {valor_total}")

# Generar reporte
reporte = generar_reporte(productos_con_descuento)
for linea in reporte:
    print(linea)
