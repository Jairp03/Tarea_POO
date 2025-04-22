class Producto:
    def __init__(
        self,
        codigo:str,
        nombre:str,
        precio:float,
        stock:int,
        categoria:str,
        tipo:str,
        fecha_vencimiento:str = "No registra",
        garantia: str = "No registra"
    ) -> None:
        self.codigo:str = codigo
        self.nombre:str = nombre
        self._precio:float = precio
        self._stock:int = stock
        self.__categoria:str = categoria
        self.tipo:str = tipo
        self.fecha_vencimiento:str = fecha_vencimiento
        self.garantia:str = garantia

    @property
    def precio (self) -> str:
        return self._precio
    @precio.setter
    def precio(self, precio:float) -> float:
        if (precio >= 0):
            self._precio = precio
        else:
            print("El precio no puede ser menor")

    
    @property
    def stock(self) -> str:
        return self._stock
    @stock.setter
    def stock(self, stock:int) -> int:
        if (stock >= 0):
            self._stock = stock
        else:
            print("El valor no debe ser negativo")
    
    @property
    def categoria(self) -> str:
        return self.__categoria
    
    def mostrar_datos(self) -> str:
        return (
            f"codigo: {self.codigo}\n"
            f"nombre: {self.nombre}\n"
            f"precio: {self._precio}\n"
            f"stock: {self._stock}\n"
            f"categoria: {self.__categoria}\n"
            f"tipo: {self.tipo}\n"
            f"fecha de vencimiento: {self.fecha_vencimiento}\n"
            f"garantia: {self.garantia}\n"
            )
            

if __name__ == "__main__":
    producto1 = Producto("2022", "Leche", 1.50, 25, "Lacteos", "Alimentos", "25/06/2025")
    producto2 = Producto("05154", "aspiradora", 550.65, 10, "impieza","Electrodomestico","", "5 meses")
    print(producto1.mostrar_datos())
    print(producto2.mostrar_datos())