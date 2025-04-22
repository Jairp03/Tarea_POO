import time
from collections import namedtuple
from functools import wraps

# --- Excepciones personalizadas ---
class ProductoError(Exception):
    pass

class StockInsuficienteError(ProductoError):
    def __init__(self, mensaje="Stock insuficiente para realizar la operación."):
        super().__init__(mensaje)

# --- Decoradores ---
def registrar_operacion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] Finalizó: {func.__name__}")
        return resultado
    return wrapper

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"[TIEMPO] {func.__name__} tomó {fin - inicio:.4f} segundos.")
        return resultado
    return wrapper

# --- Clase Producto ---
class Producto:
    def __init__(self, codigo, nombre, precio, stock, categoria, tipo, fecha_vencimiento=None, garantia=None):
        self.codigo = codigo              # Público
        self._nombre = nombre             # Protegido
        self.__precio = precio            # Privado
        self.stock = stock
        self.categoria = categoria
        self.tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.garantia = garantia

    # Propiedades para acceder al nombre y precio
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ProductoError("El precio no puede ser negativo.")
        self.__precio = nuevo_precio

    def __str__(self):
        return f"{self.nombre} (${self.precio}) - Stock: {self.stock}"

    @registrar_operacion
    def vender(self, cantidad):
        if cantidad > self.stock:
            raise StockInsuficienteError()
        self.stock -= cantidad
@registrar_operacion
def cargar_productos(lista_datos):
    productos = []
    for datos in lista_datos:
        producto = Producto(*datos)
        productos.append(producto)
    return productos
datos_productos = [
    (1, "Laptop", 1200, 10, "Electrónica", "Computadora", None, "2 años"),
    (2, "Mouse", 20, 50, "Accesorios", "Periférico"),
    (3, "Café", 5, 100, "Alimentos", "Bebida", "2025-01-01")
]

productos = cargar_productos(datos_productos)
@registrar_operacion
def aplicar_descuento(productos, porcentaje):
    return list(map(lambda p: actualizar_precio(p, porcentaje), productos))

def actualizar_precio(producto, porcentaje):
    nuevo_precio = producto.precio * (1 - porcentaje / 100)
    producto.precio = round(nuevo_precio, 2)
    return producto
@medir_tiempo
def calcular_valor_total(productos):
    return sum(p.precio * p.stock for p in productos)
@registrar_operacion
def generar_reporte(productos):
    reporte = list(map(lambda p: f"{p.codigo}: {p.nombre} - ${p.precio} x {p.stock}", productos))
    for linea in reporte:
        print(linea)
try:
    productos = cargar_productos(datos_productos)
    productos = aplicar_descuento(productos, 10)
    total = calcular_valor_total(productos)
    print(f"\nValor total del inventario: ${total:.2f}")
    generar_reporte(productos)
    productos[0].vender(5)
except ProductoError as e:
    print(f"[ERROR]: {e}")
